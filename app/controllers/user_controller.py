from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app import create_app

# Create a Blueprint for the advice routes
user_bp = Blueprint('user', __name__)

app = create_app.create_app()

@user_bp.route('/user', methods=['POST'])
@swag_from('../swagger/swagger.yml')
def createUser(): 
	data = request.json
	myUser = app.userService.createUser(data['fullName'], data['email'],
		data['password'], data['role'], data['username'], data['age'], data['avatarImg'])
	userId = str(myUser._id)
	return jsonify({ '_id': userId, 
		'fullName': myUser.fullName, 
		'email': myUser.email,
		'password': myUser.password,
		'role': myUser.role,
		'username': myUser.username,
		'age': myUser.age,
		'avatarImg': myUser.avatarImg,
		'exp': myUser.exp,
		'level': myUser.level,
		'challengesCompleted': myUser.challengesCompleted}), 201

@user_bp.route('/user/<userId>', methods=['GET'])
@swag_from('../swagger/swagger.yml')
def getUserById(userId: str):
	user = app.userService.getUserById(userId)
	if user:
		return jsonify(user), 200
	return jsonify({'error': 'User not found'}), 404

@user_bp.route('/user', methods=['GET'])
@swag_from('../swagger/swagger.yml')
def getAllUsers():
	users = app.userService.getAllUsers()
	return jsonify(users), 200

@user_bp.route('/user/<userId>', methods=['PUT'])
@swag_from('../swagger/swagger.yml')
def updateUser(userId: str):
	data = request.json
	updatedUser = app.userService.updateUser(userId, data['fullName'], data['email'],
		data['password'], data['role'], data['username'], data['age'], data['avatarImg'], data['exp'], data['level'], data['challengesCompleted'])
	return jsonify(updatedUser), 200

@user_bp.route('/user/<userId>', methods=['DELETE'])
@swag_from('../swagger/swagger.yml')
def deleteTopicr(userId: str):
	result = app.userService.deleteUser(userId)
	return jsonify(result)

@user_bp.route('/user/completeChallenge/<userId>', methods=['PUT'])
@swag_from('../swagger/swagger.yml')
def completeChallenge(userId: str):
	data = request.json
	result = app.userService.completeChallenge(userId, data['challengeId'])
	return jsonify(result)