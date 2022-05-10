from flask_sqlalchemy import SQLAlchemy
from ..app import db

db = SQLAlchemy
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)