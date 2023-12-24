from app.classes.topic import Theme
from flask import current_app
from bson.objectid import ObjectId

class TopicRepository:
	def __init__(self, app):
		self.app = app
		
	def createTheme(self, theme: Theme):
		return current_app.mongo.db.theme.insert_one(theme.__dict__)
	
	def getThemeById(self, themeId: str):
		return current_app.mongo.db.theme.find_one({'_id': ObjectId(themeId)})

	def getAllThemes(self):
		return list(current_app.mongo.db.theme.find())

	def updateTheme(self, themeId: str, updatedTheme: Theme):
		return current_app.mongo.db.theme.update_one({'_id': ObjectId(themeId)}, {'$set': updatedTheme.__dict__})

	def deleteTheme(self, themeId: str):
		return current_app.mongo.db.theme.delete_one({'_id': ObjectId(themeId)})