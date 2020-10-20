Flask Assessment Notes
Setup
I advise you to get a working app as early as possible in the assessment – even if its just a hello world text route – get a route rendered and running

Setup up virtual environment using pipenv and install all requirements
Don’t forget to activate your virtual environment using pipenv shell
Create your database / user
The test will tell you what the database/user should be called – copy / paste the names to avoid typos
Set up your configuration
The test has a long explanation of SECRET_KEY – just add it – you should plan to test your app in the browser vs just running the tests
Add your database url
Add all the boilerplate setup in init.py
import Flask, Migrate, config, routes, and db
setup app object (via Flask)
set config
register_blueprint (optional)
init_app
Migrate(app, db)
Ensure you can hit a simple route on your browser, then start to work through the README
Run your tests when you have a working app in the browser
Docs Mapping
The docs can be an overwhelming place – this is a little mapping of what libraries cover what pieces of your flask app

Library	What its used for	Doc Link
flask
Running your app
Routes (either built-in or through Blueprint – both in the Flask docs)
Templates (through Jinga)
Minimal App Startup
Routing
Blueprints
Jinga Templates
sqlalchemy & flask-sqlalchemy
Connecting to your database
Creating data models
Flask-SQLAlchemy is a library that takes care of somethings you would otherwise need to setup yourself.

During the assessment – best to start with the Flask-SQLAlchemy docs, then move on to SQLAlchemy if you’re not finding what you need.
Flask-SQLAlchemy
wtforms & flask-wtf
Forms
The only thing you’ll likely need from flask_wtf is the import FlaskForm syntax – all the validators and specific fields come from wtforms
Flask-WTF Quick Start
WTForms Basic Form Fields
WTForms Validators
alembic & flask-migrate
Data Migrations
flask-migrate is another extension that configures Alembic in the proper way to work with your app – generally during the assessment you should find what you need in the flask-migrate docs
Flask-Migrate
