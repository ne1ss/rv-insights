from flask import Flask
from flask_sqlalchemy import SQLAlchemy


flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'
db = SQLAlchemy(flask_app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable='False')
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

with flask_app.app_context():
    db.create_all()


