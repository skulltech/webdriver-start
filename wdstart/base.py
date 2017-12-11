

class BaseDriver:
	def __init__(self):
		self.driver = None
		self.name = None
		self.is_incognito = None
		self.user_agent = None
		self.profile_path = None
