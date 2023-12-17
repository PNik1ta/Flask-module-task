from app.classes.user import User
from flask import current_app
from bson.objectid import ObjectId

class UserRepository:
	def __init__(self, app):
		self.app = app
		
	def createUser(self, user: User):
		return current_app.mongo.db.user.insert_one(user.__dict__)
	
	def getUserById(self, userId: str):
		return current_app.mongo.db.user.find_one({'_id': ObjectId(userId)})

	def getAllUsers(self):
		return list(current_app.mongo.db.user.find())

	def updateUser(self, userId: str, updatedUser: User):
		return current_app.mongo.db.user.update_one({'_id': ObjectId(userId)}, {'$set': updatedUser.__dict__})

	def deleteUser(self, userId: str):
		return current_app.mongo.db.user.delete_one({'_id': ObjectId(userId)})