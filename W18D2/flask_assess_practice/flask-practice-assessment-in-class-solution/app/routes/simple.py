from flask import Blueprint, redirect, render_template
from ..forms import SimpleForm
from ..models import db, SimplePerson

bp = Blueprint("simple", __name__, "")


@bp.route("/")
def main_page():
    return render_template("main_page.html")


@bp.route("/simple-form")
def simple_form():
    form = SimpleForm()
    return render_template("simple_form.html", form=form)


@bp.route("/simple-form", methods=["POST"])
def simple_form_submit():
    form = SimpleForm()
    if form.validate_on_submit():
        # data = form.data
        # person = SimplePerson(name=data['name'], age=data['age'], bio=data['bio'])
        person = SimplePerson()
        form.populate_obj(person)
        db.session.add(person)
        db.session.commit()
        return redirect("/")
    return "Bad Data"


@bp.route("/simple-form-data")
def simple_form_data():
    # result = db.session.query(SimplePerson).filter(SimplePerson.name.startswith("M"))
    result = SimplePerson.query.filter(SimplePerson.name.like("M%"))
    return render_template("simple_form_data.html", result=result)