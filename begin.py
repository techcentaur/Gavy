import output, listen
import helper, NLPapi
import nltk, argparse



class Gavy:
    def __init__(self, listen, speak):
        """Initialises the object variables.
        """
        self.listen = listen
        self.speak = speak
        self.intro()


    def intro(self):
        """Greetings and introductions. The formalities before the real fun.
        """
        self.user = 'Ankit'
        self.name = 'Gavy'

        # self.speak.output('Are you {}?'.format(self.user))
        # response = self.listen.input()
        
        # if not helper.positive(response):
            # self.speak.output('Can you please tell me who you are?')
            # self.user = self.listen.input()
        
        self.speak.output('Hi! {user}! I am {name}'.format(user=self.user, name=self.name))
        # self.speak.output('Do you want to give me a new name?') 
        # response = self.listen.input()
        
        # if helper.positive(response):
        #     self.speak.output('What should my name be?')
        #     self.name = self.listen.input()
        #     self.speak.output('So, for this session I am {name}.'.format(name=self.name)

    def query(self):
        """Takes the query as an input and starts processing it"""
        self.speak.output('How can I help you {}'.format(self.user))
        query = self.listen.input().lower()
        
        self.process(query)


    def process(self):
        """sending the query to the NLP-api main class"""
        t1 = NLPapi.main.Main(self.query, [self.user,self.name], [self.listen,self.speak])
        
        action = t1.action_work()
        t2 = manager.TasksManager(self.listen,self.speak)
        t2.execute(action[0],action[1],self.query)



if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--terminal", help='interaction through terminal', action='store_true')
    parser.add_argument("-s", "--speech", help='interaction through speech', action='store_true')
    
    args = parser.parse_args()
    
    if args.terminal:
        listen = listen.ConsoleInput()
        speak = output.ConsoleOutput()
        gavy = Gavy(listen, speak)
        gavy.query()
    else:
        listen = listen.SpeechInput()
        with output.GTTSOutput() as speak:
            gavy = Gavy(listen, speak)
            gavy.query()
