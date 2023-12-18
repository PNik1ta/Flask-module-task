class Challenge:
	def __init__(self, title: str, description: str, level: int, exp: int, _id: str = None):
		self.title = title
		self.description = description
		self.level = level
		self.exp = exp