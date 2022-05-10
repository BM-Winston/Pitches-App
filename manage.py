from flask import Flask

from app import create_app,db

from app.models import User, Role



app = Flask(__name__)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Role = Role )
if __name__ == '__main__':
    manager.run()