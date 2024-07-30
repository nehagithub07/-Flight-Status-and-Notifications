from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    
    mongo.init_app(app)
    
    from app.api import views
    app.register_blueprint(views.bp)

    return app