from app import db, flask_app as app
from app.models import Pony, Owner
from flask import render_template, redirect, request, url_for


@app.route("/")
@app.route("/index")
def index():
    pony_count = Pony.query.count()
    return render_template("index.html", pony_count=pony_count)


@app.route("/ponies")
def ponies():
    ponies = Pony.query.all()
    return render_template("ponies.html", ponies=ponies)


@app.route("/ponies/new", methods=["GET", "POST"])
def add_pony():
    if request.method == "POST":
        pony = Pony(**request.form)
        db.session.add(pony)
        db.session.commit()
        return redirect(url_for("ponies"))
    owners = Owner.query.order_by(Owner.last_name, Owner.first_name).all()
    return render_template("pony_form.html", owners=owners)

@app.route("/ponies/<int:id>/delete", methods=["POST"])
def delete_pony(id):
    pony = Pony.query.get(id)
    db.session.delete(pony)
    db.session.commit()
    return redirect(url_for("ponies"))
