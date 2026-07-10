from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from extensions import jwt, db, bcrypt
from api.allergen.routes import allergen_bp
from api.dish.routes import dish_bp
from api.ingredient.routes import ingredient_bp 
from api.user.routes import user_bp
from api.auth.routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    jwt.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    CORS(app)
    migrate = Migrate(app, db, compare_type=True)
    
    app.register_blueprint(user_bp, url_prefix='/api/user')
    app.register_blueprint(ingredient_bp, url_prefix='/api/ingredient')
    app.register_blueprint(dish_bp, url_prefix='/api/dish')
    app.register_blueprint(allergen_bp, url_prefix='/api/allergen')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    
    from models import User, Allergen, Ingredient, Dish, DishIngredient
    from admin import setup_admin
    setup_admin(app)
    return app  

