from turtle import clear
from flask_sqlalchemy import SQLAlchemy
from ..app import db
from flask_migrate import Migrate
from .main.main import main_blueprint

db = SQLAlchemy
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)


    def __init__(self,name) -> None:

        self.name = name

    def __str__(self) -> None:
        return self.name
