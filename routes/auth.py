from flask import Blueprint, render_template, request, redirect, session
from werkzeug.security import check_password_hash
from models.user import User

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        login_input = request.form["username"]
        password = request.form["password"]

        user = User.query.filter(
            (User.username == login_input) |
            (User.email == login_input) |
            (User.mobile == login_input)
        ).first()

        if user and check_password_hash(user.password, password):
            session["admin"] = True
            return redirect("/")

        return render_template(
            "login.html",
            error="Invalid Username or Password"
        )

    return render_template("login.html")


@auth.route("/logout")
def logout():

    session.pop("admin", None)

    return redirect("/login")