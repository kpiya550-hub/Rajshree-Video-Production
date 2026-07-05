from flask import Blueprint, render_template

portfolio = Blueprint("portfolio", __name__)

@portfolio.route("/portfolio")
def portfolio_page():

    return render_template("portfolio.html")