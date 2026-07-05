from flask import Blueprint, render_template, redirect
from models.contact import Contact, db
from flask import Blueprint, render_template, redirect, session

admin = Blueprint("admin", __name__)

@admin.route("/admin")
def admin_dashboard():
    if "admin" not in session:
       return redirect("/login")

    contacts = Contact.query.order_by(Contact.id.desc()).all()

    return render_template(
        "admin.html",
        contacts=contacts
    )


@admin.route("/delete/<int:id>")
def delete_message(id):

    contact = Contact.query.get_or_404(id)

    db.session.delete(contact)

    db.session.commit()

    return redirect("/admin")