from flask import Flask, render_template, redirect, Blueprint, url_for
from app.forms import LoginForm
from app.models import User
from flask_login import LoginManager, current_user, login_user, logout_user

bp = Blueprint("session", __name__, url_prefix="/session")





@bp.route("/", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data
        user = User.query.filter(User.name == name).first()
        if not user or not user.check_password(form.password.data):
            return redirect(url_for(".login"))
        login_user(user)
        return redirect('/')
    return render_template("login.html", form=form)



@bp.route('/logout', methods=["POST"])
def logout():
    logout_user()
    return redirect(url_for('.login'))
