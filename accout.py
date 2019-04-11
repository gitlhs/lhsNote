from flask import  Blueprint,render_template
accout = Blueprint("accout",__name__)

@accout.route('/accout')
def xx():
    return "accout"

@accout.route("/login")
def login():
    return render_template("login.html")