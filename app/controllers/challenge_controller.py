from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app import create_app

# Create a Blueprint for the advice routes
challenge_bp = Blueprint('challenge', __name__)

app = create_app.create_app()

@challenge_bp.route('/challenge', methods=['POST'])
@swag_from('../swagger/swagger.yml')
def createChallenge(): 
	data = request.json
	myChallenge = app.challengeService.createChallenge(data['title'], data['description'], data['category'], data['exp'])
	challengeId = str(myChallenge._id)
	return jsonify({ '_id': challengeId, 
		'title': myChallenge.title, 
		'description': myChallenge.description,
		'category': myChallenge.category,
		'exp': myChallenge.exp}), 201

@challenge_bp.route('/challenge/<challengeId>', methods=['GET'])
@swag_from('../swagger/swagger.yml')
def getChallengeById(challengeId: str):
	challenge = app.challengeService.getChallengeById(challengeId)
	if challenge:
		return jsonify(challenge), 200
	return jsonify({'error': 'Challenge not found'}), 404

@challenge_bp.route('/challenge', methods=['GET'])
@swag_from('../swagger/swagger.yml')
def getAllChallenges():
	challenges = app.challengeService.getAllChallenges()
	return jsonify(challenges), 200

@challenge_bp.route('/challenge/<challengeId>', methods=['PUT'])
@swag_from('../swagger/swagger.yml')
def updateChallenge(challengeId: str):
	data = request.json
	updatedChallenge = app.challengeService.updateChallenge(challengeId, data['title'], data['description'], data['category'], data['exp'])
	return jsonify(updatedChallenge), 200

@challenge_bp.route('/challenge/<challengeId>', methods=['DELETE'])
@swag_from('../swagger/swagger.yml')
def deleteChallenge(challengeId: str):
	result = app.challengeService.deleteChallenge(challengeId)
	return jsonify(result)