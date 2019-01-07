from flask import Blueprint, render_template
from portfolio.models import *

mod = Blueprint('site', __name__,template_folder='templates')

@mod.route('/')
def home():
    return render_template('site/index.html')

@mod.route('/articles')
def articles():
    alldata = loadArticle.query.all()
    return render_template('site/articles.html', alldata = alldata)

@mod.route('/projects')
def projects():
    return render_template('site/projects.html')

@mod.route('/about')
def about():
    return render_template('site/about.html')

@mod.route('/signin')
def signin():
    return render_template('admin/admin.html')
@mod.route('/loadarticle/<article_id>')
def loadarticle(article_id):
    loadpost = loadArticle.query.filter_by(id=article_id).all()
    return render_template('site/load-article.html', loadpost = loadpost)
