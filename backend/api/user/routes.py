from flask import Blueprint, jsonify
from models import User
from extensions import db
from flask_jwt_extended import jwt_required



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