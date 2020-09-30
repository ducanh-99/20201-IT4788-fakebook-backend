from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_mongoengine import MongoEngine   

from src.model.db import initialize_db, db
from src.util.errors import errors
from src.routes.routes import initialize_routes
from mongoengine import connect


app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
DB_URI = 'mongodb+srv://anhndvnist:ducanh99@cluster0.znpcr.mongodb.net/fakebook?retryWrites=true&w=majority'
app.config['MONGODB_SETTINGS'] = {
    "host" : DB_URI
}



initialize_db(app)
initialize_routes(api)
