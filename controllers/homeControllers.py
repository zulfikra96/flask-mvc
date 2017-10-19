from flask import render_template
class HomeControllers(object):

    def index(self):
        return render_template('page/home.html')