from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///isodalmaz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
    specialty_id = db.Column(db.Integer, nullable=False)
    violation_amount = db.Column(db.Integer, nullable=False)
    added_date = db.Column(db.DateTime, default=datetime.utcnow)


class Object(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Specialty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class ObjectsList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, nullable=False)
    object_id = db.Column(db.Integer, nullable=False)


class Documents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    empl_id = db.Column(db.Integer, nullable=False)
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


class Violations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    empl_id = db.Column(db.Integer, nullable=False)
    violation_grade = db.Column(db.Enum(ViolationGrade), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    object_id = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, default=0)
    state = db.Column(db.Integer, default=0)


@app.route('/')
@app.route('/home')
def index():
    employees = Employee.query.order_by(Employee.violation_amount).all()
    violations = Violations.query.order_by(Violations.state).all()
    return render_template("index.html", employees=employees, violations=violations)

@app.route('/newemployee')
def newemployee():
    return render_template("newemployee.html")

@app.route('/autorization')
def autorization():
    return render_template("autorization.html")


def fill_employees():
    for i in range(10):
        employee = Employee(surname="Иванов", name="Иван", middle_name="Николаевич", passport_series=5516,
                            passport_number=126524, birth_date=datetime(i+1, i+1, i+1), pass_number=i * 10,
                            specialty_id=0, violation_amount=i)
        try:
            db.session.add(employee)
            db.session.commit()
        except:
            return "Ошибка"


def fill_objects():
    try:
        db.session.add(Object("Слесарный объект УПЦ 1"))
        db.session.add(Object("Слесарный объект УПЦ 2"))
        db.session.add(Object("Слесарный объект УПЦ 3"))
        db.session.add(Object("Слесарный объект УПЦ 4"))
        db.session.add(Object("Слесарный объект УПЦ 8"))
        db.session.add(Object("Слесарный объект УПЦ 12"))
        db.session.add(Object("Слесарный объект УПЦ 23"))
        db.session.commit()
    except:
        return "Ошибка"


def fill_specialties():
    try:
        db.session.add(Specialty("Слесарь"))
        db.session.add(Specialty("Слесарь-технолог"))
        db.session.add(Specialty("Управляющий"))
        db.session.add(Specialty("Водитель"))
        db.session.add(Specialty("Грущик"))
        db.session.add(Specialty("Шахтер"))
        db.session.add(Specialty("Охранник"))
        db.session.commit()
    except:
        return "Ошибка"


def fill_violations():
    try:
        db.session.add(
            Violations(0, violation_grade=ViolationGrade.average, date=datetime(2020, 4, 18), object_id=0, points=1))
        db.session.add(
            Violations(0, violation_grade=ViolationGrade.light, date=datetime(2020, 4, 13), object_id=2))
        db.session.add(
            Violations(1, violation_grade=ViolationGrade.average, date=datetime(2020, 4, 16), object_id=5, points=1))
        db.session.add(
            Violations(2, violation_grade=ViolationGrade.heavy, date=datetime(2020, 5, 9), object_id=2, points=2))
        db.session.add(
            Violations(4, violation_grade=ViolationGrade.heavy, date=datetime(2020, 5, 7), object_id=4, points=1))
        db.session.add(
            Violations(4, violation_grade=ViolationGrade.average, date=datetime(2020, 5, 29), object_id=1))
        db.session.commit()
    except:
        return "Ошибка"


def fill_db():
    fill_employees()
    fill_objects()
    fill_specialties()
    fill_violations()



if __name__ == "__main__":
    app.run(debug=True)