from app import db


class Pony(db.Model):
    __tablename__ = 'ponies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    birth_year = db.Column(db.Integer)
    breed = db.Column(db.String(255))
    owner_id = db.Column(db.Integer, db.ForeignKey("owners.id"))

    owner = db.relationship("Owner", back_populates="ponies")


class Owner(db.Model):
    __tablename__ = "owners"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))

    ponies = db.relationship("Pony", back_populates="owner")
