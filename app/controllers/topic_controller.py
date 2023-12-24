from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app import create_app

# Create a Blueprint for the advice routes
topic_bp = Blueprint('topic', __name__)

app = create_app.create_app()

@topic_bp.route('/topic', methods=['POST'])
@swag_from('../swagger/swagger.yml')
def createTopic(): 
	data = request.json
	myTopic = app.topicService.createTopic(data['title'], data['description'])
	topicId = str(myTopic._id)
	return jsonify({ '_id': topicId, 
		'title': myTopic.title, 
		'description': myTopic.description}), 201

@topic_bp.route('/topic/<topicId>', methods=['GET'])
@swag_from('../swagger/swagger.yml')
def getTopicById(topicId: str):
	topic = app.topicService.getTopicById(topicId)
	if topic:
		return jsonify(topic), 200
	return jsonify({'error': 'Topic not found'}), 404

@topic_bp.route('/topic', methods=['GET'])
@swag_from('../swagger/swagger.yml')
def getAllTopics():
	topics = app.topicService.getAllTopics()
	return jsonify(topics), 200

@topic_bp.route('/topic/<topicId>', methods=['PUT'])
@swag_from('../swagger/swagger.yml')
def updateTopic(topicId: str):
	data = request.json
	updatedTopic = app.topicService.updateTopic(topicId, data['title'], data['description'])
	return jsonify(updatedTopic), 200

@topic_bp.route('/topic/<topicId>', methods=['DELETE'])
@swag_from('../swagger/swagger.yml')
def deleteTopic(topicId: str):
	result = app.topicService.deleteTopic(topicId)
	return jsonify(result)