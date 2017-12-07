import nltk
import output, listen
import helper
from tasks import Manager
from NLPapi import main



class Begin:


    def __init__(self):
        """intialises the variables"""

        self.listen = listen.SpeechInput()
        self.speak = output.GTTSOutput()
        self.names()


    def begin(self):
        """takes the query as an input and starts processing it"""

        self.speak.output("How can I help you Sir")
        query = self.listen.input()
        
        query=query.lower()
        processing_task(query)


    def processing_task(self,query):
        """sending the query to the NLP-api main class"""

        task = main.Main(query, [self.user,self.name],[self.listen,self.speak])
        
        action = t1.action_work()
        main.main(action,task)


    def names(self):
        """initiats the variables and begins the converstaion"""

        self.user="Ankit"
        self.name="Gavy"

        self.speak.output("Are you " + user + " ?")
        ch = self.listen.input()

        for n in nolist :
            if n in ch:
                self.speak.output("Can you please tell me who you are?")
                self.user = listen.input()

        self.speak.input("Hi! "+user+" sir. My name is " + name)
        self.speak.input("Do you want to give me a new name")
        
        ch = self.listen.input()
        if helper.positive(ch)
            self.speak.input("What should my name be?")
            
            self.name = self.listen.input()
            self.speak.output("so, for this session I am "+name +".")




if __name__=="__main__":
    b = Begin()
    b.begin()