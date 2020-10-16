from flask import Flask, render_template
from flask_migrate import Migrate
from app.models import db, Dog
import os

app = Flask(__name__)

app.config.from_mapping({
    'SQLALCHEMY_DATABASE_URI': os.environ.get('DATABASE_URL'),
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    # We need to set 'SQLALCHEMY_TRACK_MODIFICATIONS' or we'll get an error
})
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
# allows us to use pug files in our app


@app.route('/dogs')
def show_all_dogs():
    dogs = Dog.query.all()
    # we import Dog from line 3 and can query this table in the database
    return render_template('dogs.pug', title='All the pups!', dogs=dogs)
    # return dogs[0].name


@app.route('/dogs/<int:id>')
def show_dog(id):
    dog = Dog.query.get_or_404(id)
    # shows a 404 method if nothing is found
    return dog.name


db.init_app(app) # initialize database with our app
Migrate(app, db) # connect our app with our database
