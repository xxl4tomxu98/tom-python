from flask import Flask, render_template, redirect, url_for
from config import Configuration
from app.forms import ShippingForm, LogoutForm
from flask_migrate import Migrate
from app.models import db, Package, User
from flask_login import LoginManager, login_required
from app.routes import session

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(session.bp)
db.init_app(app)
migrate = Migrate(app, db)



login = LoginManager(app)
login.login_view = "session.login"


@login.user_loader
def load_user(id):
    return User.query.get(int(id))




@app.route('/')
@login_required
def root():
    packages = Package.query.all()
    logoutform = LogoutForm()
    return render_template('package_status.html', packages=packages, logoutform = logoutform)


@app.route('/new_package', methods=['GET', 'POST'])
@login_required
def new_package():
    form = ShippingForm()
    if form.validate_on_submit():
        data = form.data
        new_package = Package(sender=data["sender_name"],
                              recipient=data["recipient_name"],
                              origin=data["origin"],
                              destination=data["destination"],
                              location=data["origin"])
        db.session.add(new_package)
        db.session.commit()
        Package.advance_all_locations()
        return redirect('/')
    return render_template('shipping_request.html', form=form)
