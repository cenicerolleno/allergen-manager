from flask import Blueprint, jsonify, request
from models import User
from extensions import db, bcrypt
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt



user_bp = Blueprint('user', __name__)



@user_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_users():
    
    try:
        users = db.session.execute(db.select(User)).scalars().all()
        users_serialized = [user.serialize() for user in users]
        return jsonify({
            'msg': 'ok',
            'users': users_serialized
        }), 200  
    except Exception as e:
        return jsonify({'error': 'Error interno del servidor'}), 500
    
@user_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user_by_id(user_id):
    
    user = db.session.get(User, user_id)

    if user is None:
        return jsonify({'msg': f'El usuario con id {user_id} no existe'}), 404
    
    return jsonify({
        'msg': 'ok',
        'user': user.serialize()
    }), 200
    
@user_bp.route('/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    

    body = request.get_json(silent=True)
    if body is None:
        return jsonify({'msg': 'Debes enviar informacion en el body'}), 400
    
    user = db.session.get(User, user_id)

    if user is None:
        return jsonify({'msg': 'Usuario no encontrado'}), 404


    current_user_email = get_jwt_identity()
    current_user = User.query.filter_by(email=current_user_email).first()
    
    if current_user.id != user_id and not current_user.is_admin:
        return jsonify({'msg': 'No tienes permisos para realizar esta acción'}), 403  

    if current_user.is_admin:
        if 'is_active' in body:
            user.is_active = body['is_active']
        if 'is_admin' in body:
            user.is_admin = body['is_admin']

       
    if 'username' in body:
        user.username = body['username']
    
    if 'email' in body:
        user.email = body['email']
    
    if 'password' in body:
        hash_password = bcrypt.generate_password_hash(body['password']).decode('utf-8')
        user.password_hash = hash_password
    
    
    db.session.commit()
    
    return jsonify({
        'msg': 'Usuario actualizado',
        'user': user.serialize()
    }), 200