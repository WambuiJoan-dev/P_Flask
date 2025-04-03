#for url definitions and view functions

from flask import Blueprint, jsonify, request, db 
from .models import User

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return 'Hello!'

@main.route('/api/status')
def status():
    return jsonify({'status': 'API is running'})

@main.route('/api/users')
def get_users():
    users = User.query_all()
    return jsonify([{'id': u.id, 'username': u.username} for u in users])

@main.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username required'}), 400
    
    user = User(username=username)
    db.session.add(user)
    db.session.commit()

    return jsonify({})

#update a user (PUT/PATCH)
@main.route('/api/users/<int:id', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.username = data.get('username', user.username)
    db.session.commit()

    return jsonify({'id': user.id, 'username': user.username})

#delete a user
@main.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': f'user User {id} deleted.'})