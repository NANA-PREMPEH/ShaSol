
from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from flask_bcrypt import Bcrypt # for password hashing
#initializing
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy()
bcrypt = Bcrypt()
# adding some functional to database modules
login_manager = LoginManager() # handle section in the background
# for logging in to access a page.
login_manager.login_view = 'users.login' # function name of a route
# for giving quick message when logged in
login_manager.login_message_category = 'info'


mail = Mail()

# importing blueprint object
from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    # grouping app instances by passing in app as arguement
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # importing blueprint object
    # Registrying application
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app