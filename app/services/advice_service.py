from app.repositories.advice_repository import AdviceRepository
from app.classes.advice import Advice
import requests

class AdviceService: 
	def __init__(self, adviceRepository: AdviceRepository):
		self.adviceRepository = adviceRepository

	def createAdvice(self, title: str, description: str, author: str):
		advice = Advice(title, description, author)
		self.adviceRepository.createAdvice(advice)
		return advice
	
	def getAdviceById(self, adviceId: str): 
		advice = self.adviceRepository.getAdviceById(adviceId)
		print(advice)
		if advice:
			return [{
				'_id': str(advice['_id']),
				'title': advice['title'],
				'description': advice['description'],
				'author': advice['author'],
			}] 
		return {'error': 'Advice not found'}, 404
	
	def getAllAdvices(self): 
		adviceList = self.adviceRepository.getAllAdvices()
		return [{
			'_id': str(advice['_id']),
			'title': advice['title'],
			'description': advice['description'],
			'author': advice['author'],
		} for advice in adviceList] 
	
	def updateAdvice(self, adviceId: str, title: str, description: str, author: str):
		updatedAdvice = Advice(title, description, author, adviceId)
		print(updatedAdvice)
		result = self.adviceRepository.updateAdvice(adviceId, updatedAdvice)
		if result.matched_count > 0:
			return {'message': 'Advice updated successfully'}
		return {'error': 'Advice not found'}, 404
	
	def getRandomAdvice(self):
		url = 'https://api.adviceslip.com/advice'
		response = requests.get(url)
		if response.status_code == 200:
			advice_data = response.json()
			return advice_data['slip']['advice']
		else:
			return 'Failed to fetch advice'
	
	def deleteAdvice(self, adviceId: str):
		result = self.adviceRepository.deleteAdvice(adviceId)
		if result.deleted_count > 0:
			return {'message': 'Advice deleted successfully'}
		return {'error': 'Advice not found'}, 404
	
	def recommendAdvice(self):
		return {'message': 'Coming soon'}


