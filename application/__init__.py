from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///geographicDB.db'
app.config['SECRET_KEY'] = 'ayooo678'

db = SQLAlchemy(app)

from application import routes