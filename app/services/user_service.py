from app.repositories.user_repository import UserRepository
from app.repositories.challenge_repository import ChallengeRepository
from app.classes.user import User

class UserService: 
	def __init__(self, userRepository: UserRepository, challengeRepository: ChallengeRepository):
		self.userRepository = userRepository
		self.challengeRepository = challengeRepository

	def createUser(self, fullname: str, email: str, password: str, role: str, username: str, age: int, avatarImg: str):
		user = User(fullname, email, password, role, username, age, avatarImg, 0, 1, 0)
		self.userRepository.createUser(user)
		return user
	
	def getUserById(self, userId: str): 
		user = self.userRepository.getUserById(userId)
		if user:
			return [{
				'_id': str(user['_id']),
				'fullName': user['fullName'],
				'email': user['email'],
				'role': user['role'],
				'username': user['username'],
				'age': user['age'],
				'avatarImg': user['avatarImg'],
				'exp': user['exp'],
				'level': user['level'],
				'challengesCompleted': user['challengesCompleted']
			}] 
		return {'error': 'User not found'}, 404
	
	def getAllUsers(self): 
		userList = self.userRepository.getAllUsers()
		return [{
			'_id': str(user['_id']),
			'fullName': user['fullName'],
			'email': user['email'],
			'role': user['role'],
			'username': user['username'],
			'age': user['age'],
			'avatarImg': user['avatarImg'],
			'exp': user['exp'],
			'level': user['level'],
			'challengesCompleted': user['challengesCompleted']
		} for user in userList] 
	
	def updateUser(self, userId: str, fullname: str, email: str, password: str, role: str, username: str, age: int, avatarImg: str, exp: int, level: int, challengesCompleted: int):
		updatedUser = User(fullname, email, password, role, username, age, avatarImg, exp, level, challengesCompleted, userId)
		result = self.userRepository.updateUser(userId, updatedUser)
		if result.matched_count > 0:
			return {'message': 'User updated successfully'}
		return {'error': 'User not found'}, 404
	
	def deleteUser(self, userId: str):
		result = self.userRepository.deleteUser(userId)
		if result.deleted_count > 0:
			return {'message': 'User deleted successfully'}
		return {'error': 'User not found'}, 404

	def completeChallenge(self, userId, challengeId):
		challenge = self.challengeRepository.getChallengeById(challengeId)
		user = self.userRepository.getUserById(userId)
		if (user.level < challenge.level):
			return {'error': 'User has not enough level'}, 403
		user.exp += challenge.exp
		if (user.exp > 200):
			user.level += 1
			user.exp -= 200
		self.updateUser(userId, user['fullName'], user['email'], user['password'], user['username'], 
						user['age'], user['avatarImg'], user['exp'], user['level'], user['challengesCompleted'])



