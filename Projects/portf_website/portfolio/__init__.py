from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_envvar('APP_SETTINGS')

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

from portfolio.admin.routes import mod
from portfolio.site.routes import mod
from portfolio.models import *

app.register_blueprint(admin.routes.mod)
app.register_blueprint(site.routes.mod)
