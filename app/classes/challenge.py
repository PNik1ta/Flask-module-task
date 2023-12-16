class Challenge:
	def __init__(self, title: str, description: str, level: str, exp: int, _id: str = None):
		self.title = title
		self.description = description
		self.level = level
		self.exp = exp