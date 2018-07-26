from flask import Flask, url_for
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)#import configuration from config.py
db = SQLAlchemy(app)#database related variables
migrate = Migrate(app, db)

from app import routes
