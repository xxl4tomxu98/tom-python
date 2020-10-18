from flask import Blueprint, render_template, redirect
from ..models import db, SimplePerson
from ..forms import SimpleForm
bp = Blueprint("simple", __name__, url_prefix="")


@bp.route("/simple-form", methods=["GET"])
def simple_get():
    form = SimpleForm()
    return render_template("simple_form.html", form=form)


@bp.route("/simple-form", methods=["POST"])
def simple_post():
    form = SimpleForm()
    if form.validate_on_submit():
        # data = form.data
        # new_person = SimplePerson(name=data['name'],
        #                           age=data['age'],
        #                           bio=data['bio'])
        new_person = SimplePerson(name=form.name.data,
                                   age=form.age.data,
                                   bio=form.bio.data)
        # new_person = SimplePerson()
        # form.populate_obj(new_person)
        db.session.add(new_person)
        db.session.commit()
        return redirect('/')
    else:
        return "Bad Data"





@bp.route('/simple-form-data')
def simple_form_data():
    # people = SimplePerson.query.filter(SimplePerson.name.startswith("M")).all()
    people = db.session.query(SimplePerson).filter(SimplePerson.name.like("M%")).all()
    print(people)
    return render_template("simple_form_data.html", people=people)
