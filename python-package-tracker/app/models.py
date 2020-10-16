from flask_sqlalchemy import SQLAlchemy
from map.map import advance_delivery, DELIVERED
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


class Package(db.Model):
    __tablename__ = 'packages'

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(255))
    recipient = db.Column(db.String(255))
    origin = db.Column(db.String(255))
    destination = db.Column(db.String(255))
    location = db.Column(db.String(255))

    @staticmethod
    def advance_all_locations():
        packages = Package.query.all()
        for package in packages:
            if package.location is not DELIVERED:
                package.location = advance_delivery(package.location, package.destination)

        db.session.commit()


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    hashed_password = db.Column(db.String(100), nullable=False)
    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
