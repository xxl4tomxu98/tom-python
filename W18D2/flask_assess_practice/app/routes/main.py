from flask import render_template, Blueprint
bp = Blueprint("main", __name__, url_prefix="")

@bp.route("/")
def index():
    return render_template("main_page.html")
