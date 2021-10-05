from flaskblog import db
import click
from flask.cli import with_appcontext

#from flaskblog import posts, users


#@click.command(name='create_tables')
#@with_appcontext
def create_tables():
    db.create_all()
