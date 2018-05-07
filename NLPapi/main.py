import nltk, tasks
from textblob import TextBlob, Word
from . import stopwords_removal, lexicons_normalization
import listen, output


class Main:
	def __init__(self, query, names, objects):		
		self.query=query
		
		self.user=names[0]
		self.name=names[1]

		self.listen=objects[0]
		self.speak=objects[1]
		
		value = self.recognised_questions()
		if not value:
			self.initial_process()

	def initial_process(self):
		q = self.query_refinement(self.query)

		if "and" in q:	
			l1 = q.split(" and ")
			q=lt1[0]

			t = self.tree_forming(list1[0])
			self.work_entity_recognition(t)

			for i in range(0,len(l1)-1):
				m1 = Main(l1[i+1])
				t1 = m1.tree_forming(l1[i+1])
				m1.work_entity_recognition(t1)

	def query_refinement(self, q):
		words=['please ','hey ']
		
		for w in words:
			if w in q:
				q = q.replace(w,"")
		for i in q:
			i = Word(i).lemmatize()
		return q

	def work_entity_recognition(self, tree):
		verb = ['open','play','check','run']
		work_on = ['github','facebook','instagram','gmail','youtube','google','reddit']

		for branch in tree:
			if branch[0] in verb:
				action = branch[0]
			elif branch[0] in work_on:
				action_on = branch[0]
		try:
			self.action.append(action)
		except:
			begin.input_data(self.name, self.user)
		try:
			self.action_on.append(action_on)
		except:
			begin.input_data(self.name, self.user)


	def recognised_questions(self):		
		if self.query.startswith("can you"):
			self.speak.output("yes, I can.")
			return true

	def tree_forming(self,q):
		q_tags=nltk.pos_tag(nltk.word_tokenize(q))
		
		tree_q = nltk.tree2conlltags(nltk.ne_chunk(q_tags))
		tree_clear_q = stopwords_removal.remove_from_tree(tree_q)
		
		return tree_clear_q

	def reprocess():
		m=Main(input("enter:"))
	
	def action_work():
		return [self.action,self.action_on]
