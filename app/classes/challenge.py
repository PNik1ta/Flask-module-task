class Challenge:
	def __init__(self, title: str, description: str, category: str, exp: int, _id: str = None):
		self.title = title
		self.description = description
		self.category = category
		self.exp = exp