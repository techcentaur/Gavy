import nltk, tasks
from textblob import TextBlob, Word
from . import stopwords_removal, lexicons_normalization
import listen, output


class Language:
    def __init__(self, args):
        self.__dict__ = args 
        self.tree_forming()


    def tree_forming(self):
        query = self.__dict__['query']

        q_tags=nltk.pos_tag(nltk.word_tokenize(query))

        par = nltk.RegexpParser('CHUNK: {<JJ>*<NN | NNS>*}')
        chunk = par.parse(q_tags)
        print(chunk)

        tree_q = nltk.tree2conlltags(chunk)