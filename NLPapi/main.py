#input - string
import nltk
from textblob import TextBlob
from textblob import Word
import stopwords_removal,lexicons_normalization

class Main:


	def __init__(self,string):
		
		string=string.lower()
		self.input=string
		
		i=self.recognised_questions()
		if i!=0:
			self.initial_process()



	def initial_process(self):
		string = self.string_refinement(self.input)

		if "and" in string:
			
			list1 = string.split(" and ")
			string=list1[0]
			
			for i in range(0,len(list1)-1):
				(m1) = Main(list1[i+1])
				(t1) = (m1).tree_forming(list1[i+1])
				(m1).work_entity_recognition((t1))

			t = self.tree_forming(list1[0])
			self.work_entity_recognition(t)



	def string_refinement(self,string):
		
		words=['please ','hey ']
		
		for w in words:
			if w in string:
				string=string.replace(w,"")
		
		for i in string:
			i=Word(i).lemmatize()

		return string



	def work_entity_recognition(self,tree):

		verb = ['open','play','check','run']
		work_on = ['github','facebook','instagram','gmail','youtube','google','reddit']

		for branch in tree:
			if branch[0] in verb:
				action=branch[0]
			elif branch[0] in work_on:
				action_on=branch[0]
		try:
			print("action"+action)
		except:
			self.initial_process(input("enter:"))
		try:
			print("action_on "+action_on)
		except:
			self.initial_process(input("enter:"))


	def recognised_questions(self):
		if self.input.startswith("can you"):
			print("yes")
			return 0


	def tree_forming(self,string):

		string=string
		
		string_tags=nltk.pos_tag(nltk.word_tokenize(string))
		
		tree_string = nltk.tree2conlltags(nltk.ne_chunk(string_tags))
		tree_clear_string = (stopwords_removal.remove_from_tree(tree_string))
		
		return tree_clear_string

	def reprocess():
		m=Main(input("enter:"))
	