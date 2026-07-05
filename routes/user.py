from flask import Blueprint, render_template, request, redirect
from models.contact import db
from models.user import User

user = Blueprint("user", __name__)

@user.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        new_user = user(
            full_name=request.form["full_name"],
            username=request.form["username"],
            email=request.form["email"],
            mobile=request.form["mobile"],
            password=request.form["password"]
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")