from crypt import methods
import imp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from twittor.route import index, login

def create_app():
    app = Flask(__name__, template_folder = 'templates')
    app.config[ "SECRET_KEY" ] = 'codeleon1982'
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
    return app
