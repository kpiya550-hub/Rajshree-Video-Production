from flask import Blueprint, render_template

gallery = Blueprint("gallery", __name__)

@gallery.route("/gallery")
def gallery_page():

    return render_template("gallery.html")