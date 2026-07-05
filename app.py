from flask import Flask, render_template
from routes.about import about
from routes.services import services
from routes.gallery import gallery
from routes.portfolio import portfolio
from routes.contact import contact


app = Flask(__name__)   # Pehle app banao

app.register_blueprint(about)   # Fir blueprint register karo
app.register_blueprint(services)
app.register_blueprint(gallery)
app.register_blueprint(portfolio)
app.register_blueprint(contact)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)