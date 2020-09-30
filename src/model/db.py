from flask_mongoengine import MongoEngine

db = None

def initialize_db(app):
    db = MongoEngine(app)