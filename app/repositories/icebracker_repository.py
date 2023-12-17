from app.classes.icebreaker import Icebreaker
from flask import current_app
from bson.objectid import ObjectId

class IcebreakerRepository:
	def __init__(self, app):
		self.app = app
		
	def createIcebreaker(self, icebreaker: Icebreaker):
		return current_app.mongo.db.icebreaker.insert_one(icebreaker.__dict__)
	
	def getIcebreakerById(self, icebreadkerId: str):
		return current_app.mongo.db.icebreaker.find_one({'_id': ObjectId(icebreadkerId)})

	def getAllIcebreakers(self):
		return list(current_app.mongo.db.icebreaker.find())

	def updateIcebreaker(self, icebreakerId: str, updatedIcebreaker: Icebreaker):
		return current_app.mongo.db.icebreaker.update_one({'_id': ObjectId(icebreakerId)}, {'$set': updatedIcebreaker.__dict__})

	def deleteIcebreaker(self, icebreakerId: str):
		return current_app.mongo.db.icebreaker.delete_one({'_id': ObjectId(icebreakerId)})