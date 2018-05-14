#pieces of data which is not relevant to the context of the data should be removed
#this function remove all the stopwords like a, is, this,the ...

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

#remove stopwords
def remove(string):
	"""to remove stop words from the string"""

	tokens=nltk.word_tokenize(string)
	
	stop = set(stopwords.words('english'))
	words = [word for word in string if not word in stop]
	words = " ".join(words)
	return words


def remove_from_tree(wtree):
	"""to remove the stopwords with the same POStag as from original string"""
	
	stop = set(stopwords.words('english'))
	
	wbrach=[]
	for wnode in wtree:
		if not wnode[0] in stop:
			wbrach.append(wnode)

	return wbrach
