from flask import Blueprint, render_template, request, redirect
from models.contact import Contact, db

contact = Blueprint("contact", __name__)

@contact.route("/contact", methods=["GET", "POST"])
def contact_page():

    if request.method == "POST":

        new_contact = Contact(
            name=request.form["name"],
            email=request.form["email"],
            phone=request.form["phone"],
            message=request.form["message"]
        )

        db.session.add(new_contact)
        db.session.commit()

        return redirect("/contact")

    return render_template("contact.html")