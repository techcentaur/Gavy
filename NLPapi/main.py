import nltk, tasks
from textblob import TextBlob, Word
from . import stopwords_removal, lexicons_normalization
import listen, output




class Main:
	def __init__(self,string, names, objects):
		"""intializes the self values and the instances of listen and output files"""
		
		self.string=string
		
		self.name=names[1]
		self.user=user[0]

		self.listen=objects[0]
		self.speak=objects[1]
		
		value = self.recognised_questions()
		if not value:
			self.initial_process()



	def initial_process(self):
		string = self.string_refinement(self.inp)

		if "and" in string:
			
			list1 = string.split(" and ")
			string=list1[0]
			
			for i in range(0,len(list1)-1):
				(m1) = Main(list1[i+1])
				(t1) = (m1).tree_forming(list1[i+1])
				(m1).work_entity_recognition((t1))

			t = self.tree_forming(list1[0])
			self.work_entity_recognition(t)



	def string_refinement(self, string):
		
		words=['please ','hey ']
		
		for w in words:
			if w in string:
				string=string.replace(w,"")
		
		for i in string:
			i=Word(i).lemmatize()

		return string



	def work_entity_recognition(self, tree):

		verb = ['open','play','check','run']
		work_on = ['github','facebook','instagram','gmail','youtube','google','reddit']

		for branch in tree:
			if branch[0] in verb:
				action=branch[0]
			elif branch[0] in work_on:
				action_on=branch[0]
		try:
			self.action.append(action)
		except:
			begin.input_data(self.name,self.user)
		try:
			self.action_on.append(action_on)
		except:
			begin.input_data(self.name,self.user)


	def recognised_questions(self):
		""""""
		
		if self.string.startswith("can you"):
			
			self.speak.l(("yes, I can. But the question is will I?"))
			return true


	def tree_forming(self,string):

		string=string
		
		string_tags=nltk.pos_tag(nltk.word_tokenize(string))
		
		tree_string = nltk.tree2conlltags(nltk.ne_chunk(string_tags))
		tree_clear_string = (stopwords_removal.remove_from_tree(tree_string))
		
		return tree_clear_string

	def reprocess():
		m=Main(input("enter:"))
	
	def action_work():
		return [self.action,self.action_on]
