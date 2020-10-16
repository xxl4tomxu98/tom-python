from flask import Flask
from app.config import Config


app = Flask(__name__)
# app is the return value of the Flask object
# we invoke the Flask object with the name of our current module
app.config.from_object(Config) 
# We set the configuration variables from Config onto our app

# print(app.config['SECRET_KEY'])
# the above line of code is to demonstrate that our secret key is stored under app.config


@app.route('/') # decorator for routes
def index(): #function passed to our decorator
    return '<h1>Sample App</h1>'
