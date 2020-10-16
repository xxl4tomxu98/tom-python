from dotenv import load_dotenv
load_dotenv()

# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.
from package_tracker import app
from app.models import User, db


with app.app_context():
    db.drop_all()
    db.create_all()

    user1 = User(name="Margot", password="password")

    db.session.add(user1)

    user2 = User(name="Charles", password="password")

    db.session.add(user2)
    db.session.commit()
