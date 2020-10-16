from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from ..models import db, Order, Table, Employee
from ..forms import LogoutForm, AssignTable
bp = Blueprint("orders", __name__, url_prefix="")


@bp.route("/")
@login_required
def index():
    taf = AssignTable()
    logoutform = LogoutForm()
    return render_template("orders.html", logoutform=logoutform, form=taf)

@bp.route("/assign", methods=["POST"])
@login_required
def assign():
    form = AssignTable()
    open_tables, servers = open_tables_and_servers()
    form.table_number.choices = [(t.id, f"Table {t.number}") for t in open_tables]
    form.employee_number.choices = [(e.id, e.name) for e in servers]
    if form.validate_on_submit():
        order = Order(
            employee_id=form.employee_number.data,
            table_id=form.table_number.data,
            finished=False
        )
        db.session.add(order)
        db.session.commit()
    return redirect(url_for('.index'))



def open_tables_and_servers():
    tables = Table.query.order_by(Table.number)
    open_orders = Order.query.filter(Order.finished == False)
    busy_table_ids = [order.table_id for order in open_orders]
    open_tables = [table for table in tables if table.id not in busy_table_ids]
    servers = Employee.query.all()
    return open_tables, servers
