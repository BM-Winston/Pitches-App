from flask_sqlalchemy import SQLAlchemy
from . import db
# from flask_migrate import Migrate
# from .main import main_blueprint

# db = SQLAlchemy
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    


    def __repr__(self):
        return f'User {self.username}'


    def __init__(self,name) -> None:

        self.name = name

    def __str__(self) -> None:
        return self.name


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'
