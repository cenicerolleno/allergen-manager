from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from extensions import jwt, db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    jwt.init_app(app)
    db.init_app(app)
    CORS(app)
    migrate = Migrate(app, db, compare_type=True)
    
    return app  