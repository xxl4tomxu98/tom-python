from flask import Blueprint, redirect, render_template, url_for
from .forms import OwnerForm, PetForm
from .models import db, Pet, PetType, Owner
from sqlalchemy.orm import joinedload

bp = Blueprint("petrack", __name__, "")


@bp.route("/")
def index():
    pets = Pet.query.order_by(Pet.name).options(joinedload(Pet.owners)).all()
    owners = Owner.query.order_by(Owner.last_name, Owner.first_name).all()
    return render_template("overview.html", pets=pets, owners=owners)


@bp.route('/pets/<int:id>', methods=["GET", "POST"])
@bp.route('/pets', methods=["GET", "POST"])
def pet_detail(id=0):
    form = PetForm()
    # Set the choices for dropdowns on pet type and owners
    form.pet_type_id.choices = [
      (type.id, type.type) for type in
      PetType.query.order_by(PetType.type).all()]

    owner_query = Owner.query.order_by(Owner.last_name, Owner.first_name)
    form.owner_id.choices = [(o.id, f"{o.last_name}, {o.first_name}")
                             for o in owner_query.all()]
    if form.validate_on_submit():
        pet = Pet.query.options(joinedload(Pet.owners)).get(id) if id else Pet()
        # Update the pet
        form.populate_obj(pet)
        # Save the pet
        db.session.add(pet)
        # Commit the change
        db.session.commit()
        return redirect(url_for(".pet_detail", id=pet.id))
    else:
        pet = Pet.query.options(joinedload(Pet.owners)).get(id) if id else Pet()
        form.process(obj=pet)
        return render_template("pet_form.html", form=form, is_update=id)


@bp.route('/owners/<int:id>', methods=["GET", "POST"])
@bp.route('/owners', methods=["GET", "POST"])
def owner_detail(id=0):
    form = OwnerForm()
    if form.validate_on_submit():
        # Get or create an owner
        owner = Owner.query.get(id) if id else Owner()
        # Update the owner
        form.populate_obj(owner)
        # Save the owner
        db.session.add(owner)
        # Commit the change
        db.session.commit()
        return redirect(url_for(".owner_detail", id=owner.id))
    else:
        # Get or create an owner
        owner = Owner.query.get(id) if id else Owner()
        # Update the form
        form.process(obj=owner)
        return render_template("owner_form.html", form=form, is_update=id)
