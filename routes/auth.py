from flask import Blueprint, render_template, request, redirect, session

auth = Blueprint("auth", __name__)

USERNAME = "admin"
PASSWORD = "rajshree123"

@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:
            session["admin"] = True
            return redirect("/admin")

        return render_template(
            "login.html",
            error="Invalid Username or Password"
        )

    return render_template("login.html")


@auth.route("/logout")
def logout():

    session.pop("admin", None)

    return redirect("/login")