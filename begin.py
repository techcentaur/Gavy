import nltk
import output, listen
import helper
from tasks import Manager
from NLPapi import main
import helper



class Gavy:
    def __init__(self, listen, speak):
        """Initialises the object variables
        """
        self.listen = listen
        self.speak = speak
        self.introduction()

    def introduction(self):
        """Greetings and introductions. The formalities before the real fun.
        """
        self.user = 'Ankit'
        self.name = 'Gavy'

        self.speak.output('Are you {}?'.format(self.user))
        response = self.listen.input()
        
        if not helper.positive(response):
            self.speak.output('Can you please tell me who you are?')
            self.user = self.listen.input()
        
        self.speak.output('Hi! {user}! I am {name}'.format(user=self.user, name=self.name))
        self.speak.output('Do you want to give me a new name?') 
        response = self.listen.input()
        
        if helper.positive(response):
            self.speak.output('What should my name be?')
            self.name = self.listen.input()
            self.speak.output('So, for this session I am {name}.'.format(name=self.name))

    def getquery(self):
        """Takes the query as an input and starts processing it
        """
        self.speak.output('How can I help you {}'.format(self.user))
        query = self.listen.input().lower()
        
        self.processing_task(query)

    def execute_query(self,query):
        """Sending the query to the NLP-api main class
        """
        task = main.Main(query, [self.user,self.name],[self.listen,self.speak])
        
        action = t1.action_work()
        main.main(action,task)



if __name__=='__main__':
    listen = listen.SpeechInput()
    with output.GTTSOutput() as speak:
        gavy = Gavy(listen, speak)
        gave.execute()
