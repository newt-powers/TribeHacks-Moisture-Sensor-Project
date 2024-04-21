from flask import Blueprint, render_template
#Importing the necessary mongo stuff


bp = Blueprint("pages",__name__)
@bp.route("/")
def home():
    return render_template("pages/home.html")
@bp.route("/about")
def about():
    return render_template("pages/about.html")
@bp.route("/data")
def data():
    return render_template("pages/data.html")