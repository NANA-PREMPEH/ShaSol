from flaskblog import db

def create_tables():
    db.create_all()