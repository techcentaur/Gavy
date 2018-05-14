#!/usr/bin/env python3

import output, listen
import helper, NLPapi
import nltk, argparse
import yaml

class Gavy:
    def __init__(self, listen, speak):
        self.listen = listen
        self.speak = speak

        with open('_config.yml', 'r') as ymlfile:
            config = yaml.load(ymlfile)
        
        self.user = config['name']['username']
        self.name = config.appname['name']['appname']

        self.intro()


    def intro(self):
        self.speak.output('Hi {user}! I am {name}.'.format(user=self.user, name=self.name))


    def query(self):
        """Takes the query as an input and starts processing it"""
        self.speak.output('How can I help you {}.'.format(self.user))
        self.query = self.listen.input().lower()
        
        self.process()


    def process(self):
        """sending the query to the NLP-api main class"""
        t1 = NLPapi.main.Main(self.query, [self.user,self.name], [self.listen,self.speak])
        
        action = t1.action_work()
        t2 = manager.TasksManager(self.listen,self.speak)
        t2.execute(action[0],action[1],self.query)

def main():
    parser = argparse.ArgumentParser(description='A CLI based virtual assistant.')
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("-t", "--terminal", help='interaction through terminal', action='store_true')
    group.add_argument("-s", "--speech", help='interaction through speech', action='store_true')
    
    args = parser.parse_args()
    
    if args.terminal:
        listen = listen.ConsoleInput()
        speak = output.ConsoleOutput()
        gavy = Gavy(listen, speak)
        gavy.query()
    else if args.speech:
        listen = listen.SpeechInput()
        with output.GTTSOutput() as speak:
            gavy = Gavy(listen, speak)
            gavy.query()



if __name__=='__main__':
    main()
