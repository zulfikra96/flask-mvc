from config.db import db

class Users(db.Model):


    __tablename__ = 'users'


    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    username = db.Column('username', db.String)
    password = db.Column('password', db.String)


    def __init__(self,id=None, username=None,password=None, name=None):
        self.id = id
        self.name = name
        self.username = username
        self.password = password

    def __repr__(self):
        return '<Users %r>' % self.id

