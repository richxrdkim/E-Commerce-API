from flask import Blueprint, jsonify, request
from models.user import User
from schemas.user_schema import user_schema, users_schema
from extensions import db

user_bp = Blueprint('users', __name__, url_prefix='/users')

# GET all users


@user_bp.route('', methods=['GET'])
def get_users():
    all_users = User.query.all()
    return jsonify(users_schema.dump(all_users))

# GET single user by id


@user_bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user_schema.dump(user))

# POST create new user


@user_bp.route('', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
        name=data['name'],
        address=data.get('address', ''),
        email=data['email']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(user_schema.dump(new_user)), 201

# PUT update user by id


@user_bp.route('/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.name = data.get('name', user.name)
    user.address = data.get('address', user.address)
    user.email = data.get('email', user.email)
    db.session.commit()
    return jsonify(user_schema.dump(user))

# DELETE user by id


@user_bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': f'User {id} deleted'})
