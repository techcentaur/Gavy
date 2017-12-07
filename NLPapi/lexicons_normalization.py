# coding=utf-8

from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
import nltk


def normalize(words):
	"""Another type of textual noise is about the multiple representations exhibited by single word, this function with settle them into single word"""	
	lem = WordNetLemmatizer()
	
	words_list=[]

	for word,tag in pos_tag(nltk.word_tokenize(words)):
		wtag = tag[0].lower()
		wtag = [wtag if wtag in ['a','r','n','v'] else None]
		word1 = lem.lemmatize(word,wtag) if wtag else None
		words_list.append(word1)
	words=" ".join(words_list)
	return words