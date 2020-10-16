from flask import Flask
from app.config import Config
from app.routes import inventory, main

app = Flask(__name__)
app.config.from_object(Config)
# print(app.config['SECRET_KEY'])

app.register_blueprint(inventory.bp)
app.register_blueprint(main.bp)
# We now no longer need to import our routes below our declaration of app
# We register our blueprints onto app, giving our app access to these routes
