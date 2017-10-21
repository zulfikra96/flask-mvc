from flask import render_template, redirect, request
from models.Users import Users
from config.db import db
import socket

class HomeControllers(object):

    def index(self):

        users = Users()
        usr = users.query.all()
        return render_template('page/home.html', users=usr)


    def delete_data(self):
        id = request.form['id']
        users = Users()
        usr = users.query.filter_by(id=id).first()
        db.session.delete(usr)
        db.session.commit()
        return redirect('/')

    def create(self):
        username    = request.form['username']
        password    = request.form['password']
        name        = request.form['name']
        
        users = Users(name=name,username=username,password=password)
        db.session.add(users)
        db.session.commit()
        return redirect('/')

    def edit(self,id):
        users = Users()
        usr     = users.query.filter_by(id=id).first()
        data = {'username' : usr.username,
                'password' : usr.password,
                'name' : usr.name,
                'id':usr.id
                } 

        return render_template('page/home.html', data=data)

    def update(self,id):
        users = Users()
        usr  = users.query.filter_by(id=id).first()
        usr.name = request.form['name']
        usr.username = request.form['username']
        usr.password = request.form['password']
        db.session.commit()
        return redirect('/')

        
