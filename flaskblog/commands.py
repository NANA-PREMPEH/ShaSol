from flaskblog import db

def create_table():
    db.create_all()