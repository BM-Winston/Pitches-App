from flask import Flask

from app import create_app,db

from app.models import User

app = Flask(__name__)