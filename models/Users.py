from config.db import db

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    username = db.Column('username', db.String)
    password = db.Column('password', db.String)