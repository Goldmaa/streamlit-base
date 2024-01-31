import persistent

class User(persistent.Persistent):
	def __init__(self, username, email, password): #  REGISTER()
		self.__username = username
		self.__email = email
		self.__password = password
		self._tamagema = persistent.list.PersistentList() # plural of tamagemon

	def __repr__(self):
		return f"User({self.username}, {self.email})"

	def get_username(self):
		return self.__username
	
	def _get_email(self):
		return self.__email
	
	def __login(self, username, password):
		return self.__username == username and self.__password == password