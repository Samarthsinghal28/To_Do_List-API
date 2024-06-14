from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv
load_dotenv()

mongo = PyMongo()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    # Set the MongoDB URI and JWT secret key from environment variables
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    print("MONGO_URI:", os.getenv('MONGO_URI'))
    print("JWT_SECRET_KEY:", os.getenv('JWT_SECRET_KEY'))

    mongo.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        # Import routes and middleware here
        from . import routes
        from . import middleware

    return app
