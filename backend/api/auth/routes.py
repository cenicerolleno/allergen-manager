from flask import Blueprint
from extensions import bcrypt, jwt, db
from models import User


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    # Implement registration logic here
    return {"message": "register endpoint working"}, 200