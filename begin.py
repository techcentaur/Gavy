import nltk
import output, listen
import helper
#from tasks import Manager
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
        
        self.query=query.lower()
        

    def processing_task(self):
        """sending the query to the NLP-api main class"""

        t1 = main.Main(self.query, [self.user,self.name],[self.listen,self.speak])
        
        action = t1.action_work()
        t2 = manager.TasksManager(self.listen,self.speak)
        t2.execute(action[0],action[1],self.query)


    def names(self):
        """initiats the variables and begins the converstaion"""

        self.user="Ankit"
        self.name="Gavy"

        self.speak.output("Are you " + self.user + " ?")
        ch = self.listen.input()

        if not helper.positive(ch):
            self.speak.output("Can you please tell me who you are?")
            self.user = listen.input()

        self.speak.output("Hi! "+self.user+" sir. My name is " + self.name)
        self.speak.output("Do you want to give me a new name")
        
        ch = self.listen.input()
        if helper.positive(ch):
            self.speak.output("What should my name be?")
            
            self.name = self.listen.input()
            self.speak.output("so, for this session I am "+self.name +".")




if __name__=="__main__":
    b = Begin()
    b.begin()