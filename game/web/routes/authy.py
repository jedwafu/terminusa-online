from flask import Blueprint, request, session
from werkzeug.security import check_password_hash
from game.db.models import PlayerModel
from game.db import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    player = PlayerModel.query.filter_by(name=data['username']).first()
    if player and check_password_hash(player.password_hash, data['password']):
        session['user_id'] = player.id
        return {'status': 'success'}, 200
    return {'error': 'Invalid credentials'}, 401

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return {'status': 'logged out'}, 200