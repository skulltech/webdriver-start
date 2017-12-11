

class BaseDriver:
	def __init__(self, name, is_incognito=False, user_agent=None, profile_path=None):
		self.driver = None
		self.name = name
		self.is_incognito = is_incognito
		self.user_agent = user_agent
		self.profile_path = profile_path
