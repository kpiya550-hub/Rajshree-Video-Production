from flask import Flask, render_template
from routes.about import about
from routes.services import services
from routes.gallery import gallery
from routes.portfolio import portfolio
from routes.contact import contact
from models.contact import db
from routes.admin import admin
from routes.auth import auth


app = Flask(__name__)   # Pehle app banao
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///rajshree.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "rajshree_video_production_secret"
db.init_app(app)
app.register_blueprint(about)   # Fir blueprint register karo
app.register_blueprint(services)
app.register_blueprint(gallery)
app.register_blueprint(portfolio)
app.register_blueprint(contact)
app.register_blueprint(admin)
app.register_blueprint(auth)
with app.app_context():
    db.create_all()
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)