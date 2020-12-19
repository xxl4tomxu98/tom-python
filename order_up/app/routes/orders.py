from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from ..models import db, Order, Table, Employee, OrderDetail, MenuItem, MenuItemType
from ..forms import LogoutForm, AssignTable
from sqlalchemy.orm import joinedload

bp = Blueprint("orders", __name__, url_prefix="")


@bp.route("/")
@login_required
def index():
    logoutform = LogoutForm()
    taf = AssignTable()
    open_tables, servers = open_tables_and_servers()
    taf.tables.choices = [(t.id, f"Table {t.number}") for t in open_tables]
    taf.employees.choices = [(e.id, e.name) for e in servers]

    open_orders = Order.query.filter(
        Order.finished == False and Order.employee_id == current_user.id
    ).options(joinedload(Order.table)).options(joinedload(Order.details, OrderDetail.menu_item))

    foods = MenuItem.query.join(MenuItemType).order_by(MenuItemType.name, MenuItem.name).options(joinedload(MenuItem.type))
    foods_by_type = {}
    for food in foods:
        if food.type.name not in foods_by_type:
            foods_by_type[food.type.name] = []
        foods_by_type[food.type.name].append(food)

    data = {'taf': taf, 'orders': open_orders, 'foods_by_type': foods_by_type}
    return render_template("orders.html", **data, logoutform=logoutform)




@bp.route("/assign_table", methods=["POST"])
@login_required
def assign():
    form = AssignTable()
    open_tables, servers = open_tables_and_servers()
    form.tables.choices = [(t.id, f"Table {t.number}") for t in open_tables]
    form.employees.choices = [(e.id, e.name) for e in servers]
    if form.validate_on_submit():
        order = Order(
            employee_id=form.employees.data,
            table_id=form.tables.data,
            finished=False
        )
        db.session.add(order)
        db.session.commit()
        return redirect(url_for('.index'))



@bp.route("/finalization/<int:id>", methods=["POST"])
@login_required
def close(id):
    order = Order.query.get(id)
    order.finished = True
    db.session.commit()
    return redirect(url_for('.index'))


def open_tables_and_servers():
    tables = Table.query.order_by(Table.number)
    open_orders = Order.query.filter(Order.finished == False)
    busy_table_ids = [order.table_id for order in open_orders]
    open_tables = [table for table in tables if table.id not in busy_table_ids]
    servers = Employee.query.all()
    return open_tables, servers