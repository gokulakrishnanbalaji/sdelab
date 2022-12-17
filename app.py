from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
DB_NAME="database.db"

class Student(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    year=db.Column(db.String(100))
    email=db.Column(db.String(100))
    dept=db.Column(db.String(100))
    regno=db.Column(db.Integer)

app=Flask(__name__)
app.config['SECRET_KEY'] = "example123"
app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/addstudent',methods=['GET','POST'])
def addstudent():
    if request.method == "POST":
        name = request.form.get('name')
        regno = request.form.get('regno')
        dept = request.form.get('dept')
        year = request.form.get('year')
        email = request.form.get('email')
        new_student= Student(name=name, regno=regno, dept=dept, year=year, email=email)
        db.session.add(new_student)
        db.session.commit()
        return redirect('/viewstudents')
    return render_template("addstudent.html")

@app.route('/viewstudents',methods=['GET'])
def view():
    students = Student.query.all()
    return render_template("viewstudent.html", students=students)

@app.route('/', methods=["GET"])
def slash():
    return redirect('/viewstudents')

if __name__=="__main__":
    app.run(debug=True)