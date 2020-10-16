from flask import Flask
from .config import Configuration
from .models import db
from .routes import main, simple
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(main.bp)
app.register_blueprint(simple.bp)
db.init_app(app)
migrate = Migrate(app, db)
