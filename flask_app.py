from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///champs.db'
db = SQLAlchemy(app)


class Champ(db.Model):
    champ = db.Column(db.String(80), primary_key=True)
    mastery = db.Column(db.String(80))

    def __init__(self, champ, mastery):
        self.champ = champ
        self.mastery = mastery

    def __repr__(self):
        return "<" + self.champ + ": " + self.mastery + ">"

current_mastery = " "

@app.route('/')
def home():
    return render_template('home.html', mastery=current_mastery)


@app.route("/signup", methods=['POST'])
def submitted():
    requested_champ = request.form['champ'].lower()
    print(requested_champ)
    champ = Champ.query.filter_by(champ=requested_champ).first()
    print(champ.mastery)
    global current_mastery
    current_mastery = champ.mastery
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)