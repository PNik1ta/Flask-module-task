from app.repositories.topic_repository import ThemeRepisitory
from app.classes.topic import Theme

class TopicService: 
	def __init__(self, themeRepository: ThemeRepisitory):
		self.themeRepository = themeRepository

	def createTheme(self, title: str, description: str):
		theme = Theme(title, description)
		self.themeRepository.createTheme(theme)
		return theme
	
	def getThemeById(self, themeId: str): 
		theme = self.themeRepository.getThemeById(themeId)
		if theme:
			return [{
				'_id': str(theme['_id']),
				'title': theme.title,
				'description': theme.description,
			}] 
		return {'error': 'Theme not found'}, 404
	
	def getAllthemes(self): 
		themeList = self.themeRepository.getAllThemes()
		return [{
			'_id': str(theme['_id']),
			'title': theme['title'],
			'description': theme['description'],
		} for theme in themeList] 
	
	def updateTheme(self, themeId: str, title: str, description: str):
		updatedTheme: Theme(title, description, themeId)
		result = self.themeRepository.updateTheme(themeId, updatedTheme)
		if result.matched_count > 0:
			return {'message': 'Theme updated successfully'}
		return {'error': 'Theme not found'}, 404
	
	def deleteTheme(self, themeId: str):
		result = self.themeRepository.deleteTheme(themeId)
		if result.deleted_count > 0:
			return {'message': 'Theme deleted successfully'}
		return {'error': 'Theme not found'}, 404


