from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLAlchemy_DATABASE_URI'] = 'postgresql://postgres:postgres123@localhost/articles_db'

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(80))
    email = db.Column(db.String(50), unique=True)
    article = db.Column(db.String())
#    created_at = db.Column(db.DateTime, default=datetime.now())

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/loadarticle')
def loadarticle():
    return render_template('load-article.html')


if __name__=='__main__':
    app.run(debug=True)
