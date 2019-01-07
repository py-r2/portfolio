from flask import Blueprint, render_template, request, redirect, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from portfolio import app

mod = Blueprint('admin',__name__,template_folder='templates')
# admin = Admin(mod)

from portfolio.models import *
from portfolio.admin.forms import *
# from portfolio import db

# admin.add_view(ModelView(loadArticle,db.session))
# admin.add_view(ModelView(loadUserData,db.session))
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return storeUserData.query.get(int(user_id))

@mod.route('/admin')
def admin():
    return render_template('admin/admin.html')

'''verifying password match with module login_user of flask_login library and
in case of success redirect to a bootstrap dashboard page'''

@mod.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = storeUserData.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user,remember=form.remember.data)
                return redirect(url_for('admin.dashboard'))
        return '<h1>Invalid username or password.</h1>'
    return render_template('admin/signin.html', form=form)

'''adding new_user in to database with a generated hash password
(used werkzeug.security library) so you don't see the password in clear, just in
case someone queries the database'''

@mod.route('/signup', methods=['GET','POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = storeUserData(username=form.username.data, password=hashed_password,
        email=form.email.data)#, company=form.company.data)
        db.session.add(new_user)
        db.session.commit()
        return '<h1> New user has been created.</h1>'
    return render_template('admin/signup.html', form=form)

@mod.route("/logout")
@login_required #using module login_required to verify if you are logged in or not
def logout():
    logout_user()
    return redirect(url_for('admin.admin'))

@mod.route('/dashboard')
@login_required
def dashboard():
    return render_template('admin/dashboard.html', name=current_user.username)





@mod.route('/write', methods=['GET','POST'])
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
    return render_template('admin/write-article.html')

@mod.route('/edit', methods=['GET','POST'])
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
    return render_template('admin/edit-article.html' , all_articles = all_articles)

@mod.route('/editarticle/<article_id>')
def editarticle(article_id):
    data = loadArticle.query.filter_by(id=article_id).all()
    return render_template('admin/edit-article.html' , data = data)
