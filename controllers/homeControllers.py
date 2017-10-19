from flask import render_template
from models.Users import Users

class HomeControllers(object):

    def index(self):

        users = Users()
        usr = users.query.all()
        return render_template('page/home.html', users=usr)