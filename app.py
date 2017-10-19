from flask import Flask
from config.db import db
from routes.route import route


app = Flask(__name__)
try:
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@127.0.0.1/crud_python"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
except ValueError as e:
    pass

app.register_blueprint(route)

app.run(debug=True)