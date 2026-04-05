from flask import Flask
from flask_cors import CORS
from config import Config
from app import extensions
from pymongo import MongoClient

def create_app():
    # 1. Initialize the core app engine
    app = Flask(__name__)
    
    # 2. Load the settings (like your MongoDB password) from config.py
    app.config.from_object(Config)
    
    # 3. Add CORS so your Next.js frontend is allowed to talk to it
    CORS(app)

    # 4. Fill the empty database boxes we made in extensions.py
    extensions.mongo_client = MongoClient(app.config["MONGO_URI"])
    extensions.db = extensions.mongo_client[app.config["DB_NAME"]]

    # 5. Go to the Registration Desk (File 6) and plug in the Traffic Cop (File 5)
    from app.routes import register_routes
    register_routes(app)

    return app