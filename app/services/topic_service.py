from app.repositories.topic_repository import TopicRepository
from app.classes.topic import Topic

class TopicService: 
	def __init__(self, topicRepository: TopicRepository):
		self.topicRepository = topicRepository

	def createTopic(self, title: str, description: str):
		topic = Topic(title, description)
		self.topicRepository.createTopic(topic)
		return topic
	
	def getTopicById(self, topicId: str): 
		topic = self.topicRepository.getTopicById(topicId)
		if topic:
			return [{
				'_id': str(topic['_id']),
				'title': topic['title'],
				'description': topic['description'],
			}] 
		return {'error': 'Topic not found'}, 404
	
	def getAllTopics(self): 
		topicList = self.topicRepository.getAllTopics()
		return [{
			'_id': str(topic['_id']),
			'title': topic['title'],
			'description': topic['description'],
		} for topic in topicList] 
	
	def updateTopic(self, topicId: str, title: str, description: str):
		updatedTopic = Topic(title, description, topicId)
		result = self.topicRepository.updateTopic(topicId, updatedTopic)
		if result.matched_count > 0:
			return {'message': 'Topic updated successfully'}
		return {'error': 'Topic not found'}, 404
	
	def deleteTopic(self, topicId: str):
		result = self.topicRepository.deleteTopic(topicId)
		if result.deleted_count > 0:
			return {'message': 'Topic deleted successfully'}
		return {'error': 'Topic not found'}, 404


