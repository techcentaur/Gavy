from . import github, google, reddit, youtube
from selenium import webdriver



class TasksManager:
	def __init__(self, listen, speak):
		self.driver = webdriver.Firefox()
		self.listen = listen
		self.speak = speak

	def __validate(action, obj, query):
		actions = {
			'open': ['github', 'instagram', 'gmail', 'reddit', 'facebook'], 
			'play': ['youtube'], 
			'google': ['google']
		}
		
		if action in actions:
			if obj in actions[action]:
				return True
		return False

	def execute(action, obj, query):
		if not __validate(action, obj, query):
			self.speak.output("Sorry! I don't know how to do that!")
			return

		if action=='open':
			if j=='github':
				github.open(self.driver, self.listen, self.speak)
			elif j=='instagram':
				instagram.open(self.driver, self.listen, self.speak)
			elif j=='gmail':
				gmail.open(self.driver, self.listen, self.speak)
			elif j=='reddit':
				reddit.open(self.driver, self.listen, self.speak)
			elif j=='facebook':
				facebook.open(self.driver, self.listen, self.speak)
			
		elif i=='play':
			if j=='youtube':
				youtube.play(query)
