from portfolio import db
from sqlalchemy import Column, Integer, DateTime
from flask_login import UserMixin
import datetime

class loadArticle(db.Model):
    __tablename__="data"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20))
    title = db.Column(db.String(200), unique=True)
    article = db.Column(db.String(3000))
    date_posted = db.Column(db.Date(), default=datetime.datetime.now)

    def __init__(self,user_name,title,article,date):
        self.user_name = user_name
        self.title = title
        self.article = article
        self.date = date

'''class loadUserData(db.Model):
    __tablename__="userdata"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(20))
    email = db.Column(db.String(50), unique=True)'''

#define database model by inheriting from UserMixin user class properties and methods
class storeUserData(UserMixin, db.Model):
    __tablename__="userdata"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(20))
    email = db.Column(db.String(50), unique=True)
    company = db.Column(db.String(120))
