from flask import Blueprint, render_template
from models.contact import Contact

admin = Blueprint("admin", __name__)

@admin.route("/admin")
def admin_dashboard():

    contacts = Contact.query.all()

    return render_template(
        "admin.html",
        contacts=contacts
    )