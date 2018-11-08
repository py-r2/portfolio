''' This is my personal portfolio/blog website which you can use for free
to create your own portfolio website. '''

from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, DateTime
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dbusername:dbpassword@localhost/dbname'
db = SQLAlchemy(app)

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

class loadUserData(db.Model):
    __tablename__="userdata"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(20))
    email = db.Column(db.String(50), unique=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/articles')
def articles():
    alldata = loadArticle.query.all()
    return render_template('articles.html', alldata = alldata)

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/loadarticle/<article_id>')
def loadarticle(article_id):
    loadpost = loadArticle.query.filter_by(id=article_id).all()
    return render_template('load-article.html', loadpost = loadpost)

@app.route('/write', methods=['GET','POST'])
def write_to_database():
    if request.method == 'POST':
        name = request.form["user_name"]
        title = request.form["article_title"]
        article = request.form["article_body"]
        date = datetime.datetime.now()
        if db.session.query(loadArticle).filter(loadArticle.title==title).count() == 0:
            store_article = loadArticle(name,title,article,date)
            db.session.add(store_article)
            db.session.commit()
            return '<h1> New article has been created.</h1>'
        else:
            return '<h1> There is one another article with this title in your database already! </h1>'
    return render_template('write-article.html')

@app.route('/edit', methods=['GET','POST'])
def edit_to_database():
    all_articles = loadArticle.query.all()
    if request.method == 'POST':
        name_new = request.form["user_name"]
        title_new = request.form["article_title"]
        article_new = request.form["article_body"]
        date_new = datetime.datetime.now()
        data_id = request.form["article_id"]
        if db.session.query(loadArticle).filter(loadArticle.title==title_new).count() == 1:
            loadArticle.query.filter_by(id=data_id).delete()
            store_article = loadArticle(name_new,title_new,article_new,date_new)
            db.session.add(store_article)
            db.session.commit()
            return '<h1> Your article has been updated.</h1>'
    return render_template('edit-article.html' , all_articles = all_articles)

@app.route('/editarticle/<article_id>')
def editarticle(article_id):
    data = loadArticle.query.filter_by(id=article_id).all()
    return render_template('edit-article.html' , data = data)


if __name__=='__main__':
    app.run(debug=True)
