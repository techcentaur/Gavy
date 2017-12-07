from . import github, google, reddit, youtube
from selenium import webdriver



class TasksManager:
	def __init__(self, inp, opt):
		self.driver = webdriver.Firefox()
		self.inp = inp
		self.opt = opt

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
			self.opt.output("Sorry! I don't know how to do that!")
			return

		if action=='open':
			if j=='github':
				github.open(self.driver, self.inp, self.opt)
			elif j=='instagram':
				instagram.open(self.driver, self.inp, self.opt)
			elif j=='gmail':
				gmail.open(self.driver, self.inp, self.opt)
			elif j=='reddit':
				reddit.open(self.driver, self.inp, self.opt)
			elif j=='facebook':
				facebook.open(self.driver, self.inp, self.opt)
			
		elif i=='play':
			if j=='youtube':
				youtube.play(query)
