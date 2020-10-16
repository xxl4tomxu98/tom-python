from flask import Flask

app = Flask(__name__)

from app import routes # noqa
# We need to import routes below where we setup our routes because routes will import app
# This is an anti-pattern we will fix later
# noqa will tell the linter to ignore this
