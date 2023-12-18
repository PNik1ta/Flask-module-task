from app.repositories.icebracker_repository import IcebreakerRepository
from app.classes.icebreaker import Icebreaker

class IcebreakerService: 
	def __init__(self, icebreakerRepository: IcebreakerRepository):
		self.icebreakerRepository = icebreakerRepository

	def createIcebreaker(self, title: str, description: str, category: str):
		icebreaker = Icebreaker(title, description, category)
		self.icebreakerRepository.createIcebreaker(icebreaker)
		return icebreaker
	
	def getAdviceById(self, icebreadkerId: str): 
		icebreaker = self.icebreakerRepository.getIcebreakerById(icebreadkerId)
		if icebreaker:
			return [{
				'_id': str(icebreaker['_id']),
				'title': icebreaker.title,
				'description': icebreaker.description,
				'category': icebreaker.category,
			}] 
		return {'error': 'Icebreaker not found'}, 404
	
	def getAllIcebreakers(self): 
		icebreakerList = self.icebreakerRepository.getAllIcebreakers()
		return [{
			'_id': str(icebreaker['_id']),
			'title': icebreaker.title,
			'description': icebreaker.description,
			'category': icebreaker.category,
		} for icebreaker in icebreakerList] 
	
	def updateIcebreaker(self, icebreakerId: str, title: str, description: str, category: str):
		updatedIcebreaker: Icebreaker(title, description, category, icebreakerId)
		result = self.icebreakerRepository.updateIcebreaker(icebreakerId, updatedIcebreaker)
		if result.matched_count > 0:
			return {'message': 'Icebreaker updated successfully'}
		return {'error': 'Icebreaker not found'}, 404
	
	def deleteIcebreaker(self, icebreakerId: str):
		result = self.icebreakerRepository.deleteIcebreaker(icebreakerId)
		if result.deleted_count > 0:
			return {'message': 'Icebreaker deleted successfully'}
		return {'error': 'Icebreaker not found'}, 404


