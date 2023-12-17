from app.classes.challenge import Challenge
from flask import current_app
from bson.objectid import ObjectId

class ChallengeRepository:
	def __init__(self, app):
		self.app = app
		
	def createChallenge(self, challenge: Challenge):
		return current_app.mongo.db.challenge.insert_one(challenge.__dict__)
	
	def getChallengeById(self, challengeId: str):
		return current_app.mongo.db.challenge.find_one({'_id': ObjectId(challengeId)})

	def getAllChallenges(self):
		return list(current_app.mongo.db.challenge.find())

	def updateChallenge(self, challengeId: str, updatedChallenge: Challenge):
		return current_app.mongo.db.challenge.update_one({'_id': ObjectId(challengeId)}, {'$set': updatedChallenge.__dict__})

	def deleteChallenge(self, challengeId: str):
		return current_app.mongo.db.challenge.delete_one({'_id': ObjectId(challengeId)})