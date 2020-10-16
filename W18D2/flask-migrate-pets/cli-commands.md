# SQLALchemy documentation

* https://flask-sqlalchemy.palletsprojects.com/en/2.x/



# CLI Commands

## What Packages to Install

`pipenv install Flask Flask-SQLAlchemy Psycopg2-binary alembic Flask-Migrate python-dotenv pypugjs`

* Flask creates flask app

* Flask-SQLAlchemy integrates SQLAlchemy to our application

* Psycopg2-binary allows SQLAlchemy to connect to our databse

* alembic manages our migrations

* Flask-Migrate integrate alembic with our flask app

* python-dotenv access our enviornment variables we will store in `.flaskenv` and `.env`

* pypugjs allows us to use pug files


## Create Database

1. Enter postgres

2. `create user <username> with createdb password '<password>'`;

3. `create database <db_name> with owner <username>`;

4. exit postgres





1. `pipenv run flask db init`
    * initializes the database for our application
    * auto generates migrations folder

2. `pipenv run flask db migrate -m '<semantic message>'`
    * generates a migration file based off our models

3. `pipenv run flask db upgrade`
    * applies our migrations to the database

4. `pipenv run flask db downgrade <revision id to revert to>`
    * reverts to a prior migration
