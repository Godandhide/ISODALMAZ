from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///isodalmaz.db'
app.config['AQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(25), nullable=False)
    name = db.Column(db.String(25), nullable=False)
    middle_name = db.Column(db.String(25), nullable=False)
    passport_number = db.Column(db.Integer, nullable=False)
    passport_series = db.Column(db.Integer, nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    pass_number = db.Column(db.Integer, nullable=False)
    object_id = db.Column(db.Integer, nullable=False)
    specialty_id = db.Column(db.Integer, nullable=False)
    violation_amount = db.Column(db.Integer, nullable=False)
    added_date = db.Column(db.DateTime, default=datetime.utcnow)


class Object(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Specialty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class ViolationsList(db.Model):
    employee_id = db.Column(db.Integer, nullable=False)
    violation_id = db.Column(db.Integer, nullable=False)


class DocumentsList(db.Model):
    employee_id = db.Column(db.Integer, nullable=False)
    document_id = db.Column(db.Integer, nullable=False)


class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    verified = db.Column(db.Boolean, default=False)
    doc_type_id = db.Column(db.Integer, nullable=False)
    validity = db.Column(db.DateTime, nullable=False)


class DocTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class ViolationGrade(enum.Enum):
    light = 1
    average = 2
    heavy = 3


class Violation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    violation_grade = db.Column(db.Enum(ViolationGrade), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    object_id = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, default=0)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/vova')
def vova():
    return render_template("index_vova.html")

@app.route('/newemployee')
def newemployee():
    return render_template("newemployee.html")

@app.route('/newemployee')
def newemployee():
    return render_template("newemployee.html")


if __name__ == "__main__":
    app.run(debug=True)