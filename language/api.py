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

        tree_q = nltk.tree2conlltags(chunk)
        langlist = []

        print(tree_q)
        for tup in tree_q:
            if tup[1] == 'VB':
                string = tup[0]
            elif tup[2] == "B-CHUNK" or tup[2] == "I-CHUNK":
                string += tup[0]
            else:
                continue
            langlist.append(string)
            string = ""

        print(langlist)