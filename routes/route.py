from flask import Blueprint, render_template, request
from controllers.homeControllers import *
from models.Users import Users

route = Blueprint('route',__name__,template_folder='../views', static_folder='../assets')
                    

@route.route('/')
def index():
    home = HomeControllers() 
    return home.index()

@route.route('/create', methods=['POST', 'GET'])
def create():
    user = Users()
    home = HomeControllers()
    if request.method == 'GET':
        return str(user.query.first().name)
    elif request.method == 'POST':
        return home.create()

@route.route('/test/delete/', methods=['POST'])
def delete_data():
    home = HomeControllers()
    if request.method == 'POST':
        return home.delete_data()

@route.route('/edit/<id_data>', methods=['GET'])
def edit(id_data):
    home = HomeControllers()
    return home.edit(id_data)

@route.route('/edit/<id_data>', methods=['POST'])
def update(id_data):
    home = HomeControllers()
    return home.update(id_data)