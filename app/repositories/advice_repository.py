from app.classes.advice import Advice
from flask import current_app
from bson.objectid import ObjectId

class AdviceRepository:
	def __init__(self, app):
		self.app = app
		
	def createAdvice(self, advice: Advice):
		return current_app.mongo.db.advice.insert_one(advice.__dict__)
	
	def getAdviceById(self, adviceId: str):
		return current_app.mongo.db.advice.find_one({'_id': ObjectId(adviceId)})

	def getAllAdvices(self):
		return list(current_app.mongo.db.advice.find())

	def updateAdvice(self, adviceId: str, updatedAdvice: Advice):
		return current_app.mongo.db.advice.update_one({'_id': ObjectId(adviceId)}, {'$set': updatedAdvice.__dict__})

	def deleteAdvice(self, adviceId: str):
		return current_app.mongo.db.advice.delete_one({'_id': ObjectId(adviceId)})