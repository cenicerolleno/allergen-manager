from flask import Blueprint, request, jsonify
from extensions import bcrypt, db
from models import User
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token    


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():

    body = request.get_json(silent=True )
    
    if body is None:
        return jsonify({'msg': 'Debes enviar informacion en el body'}), 400
    
    if 'username' not in body:
        return jsonify({'msg': 'Debes proporcionar un nombre de usuario'}), 400
    
    if 'email' not in body:
        return jsonify({'msg': 'Debes proporcionar un correo electrónico'}), 400
    if 'password' not in body:
        return jsonify({'msg': 'Debes proporcionar una contraseña'}), 400
    
    new_register = User()
    new_register.username = body['username']
    new_register.email = body['email']
    hash_password = bcrypt.generate_password_hash(body['password']).decode('utf-8')
    new_register.password_hash = hash_password
    new_register.is_active = True
    
    try:
        db.session.add(new_register)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'msg': 'Ya existe un usuario con ese email'}), 400
   
    return jsonify({'msg': 'Usuario registrado!', 'register': new_register.serialize()}), 200


@auth_bp.route('/login', methods=['POST'])
def login():
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({'msg': 'Debes enviar informacion en el body'}), 400

    if 'email' not in body:
        return jsonify({'msg': 'Debes proporcionar un correo electrónico'}), 400

    if 'password' not in body:
        return jsonify({'msg': 'Debes proporcionar una contraseña'}), 400

    user = User.query.filter_by(email=body['email']).first()

    if user is None:
        return jsonify({'msg': 'Usuario o contraseña incorrecta'}), 400
    
    if not bcrypt.check_password_hash(user.password_hash, body['password']):
        return jsonify({'msg': 'Usuario o contraseña incorrecta'}), 400
    
    access_token = create_access_token(
        identity=user.email,
        additional_claims={'is_admin': user.is_admin}
        )
    return jsonify({
        'msg': 'Login exitoso', 
        'token': access_token
        }), 200