from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

weblogin=Flask(__name__)
weblogin.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/weblogin_db1'
db=SQLAlchemy(weblogin)

#creates database table with SQLAlchemy
class loadData(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    username_=db.Column(db.String(120))
    password_=db.Column(db.String(20), unique=True)
    email_=db.Column(db.String(120), unique=True)
    company_=db.Column(db.String(120))

    def __init__(self, username_, password_, email_, company_):
        self.username_=username_
        self.password_=password_
        self.email_=email_
        self.company_=company_

@weblogin.route("/")
def index():
    return render_template("index.html")

@weblogin.route("/create", methods=['POST'])
def create():
    if request.method=='POST':
        name=request.form["user_name"]
        password=request.form["user_password"]
        email=request.form["email_address"]
        company=request.form["company_name"]
        if db.session.query(loadData).filter(loadData.email_==email).count() == 0:
            loaddata=loadData(name,password,email,company)
            db.session.add(loaddata)
            db.session.commit()
            return render_template("success.html")
    return render_template('create.html')

@weblogin.route("/login", methods=['POST'])
def login():
    if request.method=='POST':
        password=request.form["user_password"]
        email=request.form["email_address"]
        if (db.session.query(loadData).filter(loadData.email_==email).count() == 1) and (db.session.query(loadData).filter(loadData.password_==password).count() == 1):
            return render_template("success.html")
        else:
            return render_template("create.html")

if __name__ == '__main__':
    weblogin.degug=True
    weblogin.run()
