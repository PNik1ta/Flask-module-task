from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app import create_app

# Create a Blueprint for the advice routes
advice_bp = Blueprint('advice', __name__)

app = create_app.create_app()

@advice_bp.route('/advice', methods=['POST'])
@swag_from('../swagger/swagger.yml')
def createAdvice(): 
	data = request.json
	myAdvice = app.adviceService.createAdvice(data['title'], data['description'], data['author'])
	adviceId = str(myAdvice._id)
	return jsonify({ '_id': adviceId, 
		'title': myAdvice.title, 
		'description': myAdvice.description,
		'author': myAdvice.author}), 201

@advice_bp.route('/advice/<adviceId>', methods=['GET'])
def getAdviceById(adviceId: str):
	advice = app.adviceService.getAdviceById(adviceId)
	if advice:
		return jsonify(advice), 200
	return jsonify({'error': 'Advice not found'}), 404

@advice_bp.route('/advice', methods=['GET'])
@swag_from('../swagger/swagger.yml')
def getAllAdvices():
	advices = app.adviceService.getAllAdvices()
	return jsonify(advices), 200

@advice_bp.route('/advice/<adviceId>', methods=['PUT'])
def updateAdvice(adviceId: str):
	data = request.json
	updatedAdvice = app.adviceService.updateAdvice(adviceId, data['title'], data['description'], data['author'])
	return jsonify(updatedAdvice), 200

@advice_bp.route('/advice/<adviceId>', methods=['DELETE'])
def deleteAdvice(adviceId: str):
	result = app.adviceService.deleteAdvice(adviceId)
	return jsonify(result)