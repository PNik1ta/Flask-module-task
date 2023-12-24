from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app import create_app

# Create a Blueprint for the advice routes
icebreadker_bp = Blueprint('icebreaker', __name__)

app = create_app.create_app()

@icebreadker_bp.route('/icebreaker', methods=['POST'])
@swag_from('../swagger/swagger.yml')
def createIcebreaker(): 
	data = request.json
	myIcebreaker = app.icebreakerService.createIcebreaker(data['content'], data['category'])
	icebreakerId = str(myIcebreaker._id)
	return jsonify({ '_id': icebreakerId, 
		'content': myIcebreaker.content, 
		'category': myIcebreaker.category}), 201

@icebreadker_bp.route('/icebreaker/<icebreakerId>', methods=['GET'])
@swag_from('../swagger/swagger.yml')
def getIcebreakerById(icebreakerId: str):
	icebreaker = app.icebreakerService.getIcebreakerById(icebreakerId)
	if icebreaker:
		return jsonify(icebreaker), 200
	return jsonify({'error': 'Icebreaker not found'}), 404

@icebreadker_bp.route('/icebreaker', methods=['GET'])
@swag_from('../swagger/swagger.yml')
def getAllIcebreakers():
	icebreakers = app.icebreakerService.getAllIcebreakers()
	return jsonify(icebreakers), 200

@icebreadker_bp.route('/icebreaker/<icebreakerId>', methods=['PUT'])
@swag_from('../swagger/swagger.yml')
def updateIcebreaker(icebreakerId: str):
	data = request.json
	updatedIcebreaker = app.icebreakerService.updateIcebreaker(icebreakerId, data['content'], data['category'])
	return jsonify(updatedIcebreaker), 200

@icebreadker_bp.route('/icebreaker/<icebreakerId>', methods=['DELETE'])
@swag_from('../swagger/swagger.yml')
def deleteIcebreaker(icebreakerId: str):
	result = app.icebreakerService.deleteIcebreaker(icebreakerId)
	return jsonify(result)