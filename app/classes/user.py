class User:
	def __init__(self, fullName: str, email: str, password: str, username: str, 
			age: int, avatarImg: str, exp: int, level: int, challengesCompleted: int, _id: str = None):
		self.fullName = fullName
		self.email = email
		self.username = username
		self.password = password
		self.age = age
		self.avatarImg = avatarImg
		self.exp = exp
		self.level = level
		self.challengesCompleted = challengesCompleted