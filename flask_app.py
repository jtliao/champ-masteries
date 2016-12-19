from flask import Flask, redirect, render_template, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="jtliao",
    password="dbpassword",
    hostname="jtliao.mysql.pythonanywhere-services.com",
    databasename="jtliao$masteries",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299

db = SQLAlchemy(app)

class ChampMastery(db.Model):

    __tablename__ = "masteries"

    champ = db.Column(db.String(700), primary_key=True)
    mastery = db.Column(db.String(700))

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=comments)
    request.input["champion"]
    return redirect(url_for('index'))
    return render_template("main_page.html", masteries=db.query.all())

@app.route('/wibble')
def wibble():
    return 'This will be where masteries are'

#dbpassword
