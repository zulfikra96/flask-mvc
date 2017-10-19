from flask import Blueprint, render_template
from controllers.homeControllers import *
from models.Users import Users

route = Blueprint('route',__name__,template_folder='../views', static_folder='../assets')
                    

@route.route('/')
def index():
    home = HomeControllers() 
    return home.index()

@route.route('/create')
def create():
    user = Users()
    return str(user.query.first().id)