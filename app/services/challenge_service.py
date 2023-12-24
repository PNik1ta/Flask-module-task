from app.repositories.challenge_repository import ChallengeRepository
from app.classes.challenge import Challenge

class ChallengeService: 
	def __init__(self, challengeRepository: ChallengeRepository):
		self.challengeRepository = challengeRepository

	def createChallenge(self, title: str, description: str, category: str, exp: int):
		challenge = Challenge(title, description, category, exp)
		self.challengeRepository.createChallenge(challenge)
		return challenge
	
	def getChallengeById(self, challengeId: str): 
		challenge = self.challengeRepository.getChallengeById(challengeId)
		if challenge:
			return [{
				'_id': str(challenge['_id']),
				'title': challenge.title,
				'description': challenge.description,
				'category': challenge.category,
				'exp': challenge.exp
			}] 
		return {'error': 'Challenge not found'}, 404
	
	def getAllChallenges(self): 
		challengeList = self.challengeRepository.getAllChallenges()
		return [{
			'_id': str(challenge['_id']),
			'title': challenge.title,
			'description': challenge.description,
			'category': challenge.category,
			'exp': challenge.exp
		} for challenge in challengeList] 
	
	def updateChallenge(self, challengeId: str, title: str, description: str, category: str, exp: int):
		updatedChallenge: Challenge(title, description, category, exp, challengeId)
		result = self.challengeRepository.updateChallenge(challengeId, updatedChallenge)
		if result.matched_count > 0:
			return {'message': 'Challenge updated successfully'}
		return {'error': 'Challenge not found'}, 404
	
	def deleteChallenge(self, challengeId: str):
		result = self.challengeRepository.deleteChallenge(challengeId)
		if result.deleted_count > 0:
			return {'message': 'Challenge deleted successfully'}
		return {'error': 'Challenge not found'}, 404


