from app.classes.topic import Topic
from flask import current_app
from bson.objectid import ObjectId

class TopicRepository:
	def __init__(self, app):
		self.app = app
		
	def createTopic(self, topic: Topic):
		return current_app.mongo.db.topic.insert_one(topic.__dict__)
	
	def getTopicById(self, topicId: str):
		return current_app.mongo.db.topic.find_one({'_id': ObjectId(topicId)})

	def getAllTopics(self):
		return list(current_app.mongo.db.topic.find())

	def updateTopic(self, topicId: str, updatedTopic: Topic):
		return current_app.mongo.db.topic.update_one({'_id': ObjectId(topicId)}, {'$set': updatedTopic.__dict__})

	def deleteTopic(self, topicId: str):
		return current_app.mongo.db.topic.delete_one({'_id': ObjectId(topicId)})