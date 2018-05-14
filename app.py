#!/usr/bin/env python3

import yaml
import output, listen
import nltk, argparse
from language import api

class Gavy:
    def __init__(self, listen, speak):
        self.listen = listen
        self.speak = speak

        with open('_config.yml', 'r') as ymlfile:
            config = yaml.load(ymlfile)
        
        self.username = config['name']['username']
        self.appname = config['name']['appname']

        self.intro()


    def intro(self):
        self.speak.output('Hi {user}! I am {name}.'.format(user=self.username, name=self.appname))


    def query(self):
        self.speak.output('How can I help you {} ?'.format(self.username))
        query = self.listen.input().lower()
        
        param_dict = dict(query = query, username = self.username, appname = self.appname, input = self.listen, output = self.speak)
        lang = api.Language(param_dict)


        action = t1.action_work()
        t2 = manager.TasksManager(self.listen,self.speak)
        t2.execute(action[0],action[1],self.query)



if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Gavy: A CLI based virtual assistant.')
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("-t", "--terminal", help='interaction through terminal', action='store_true')
    group.add_argument("-s", "--speech", help='interaction through speech', action='store_true')
    
    args = parser.parse_args()
    
    if args.terminal:
        listen = listen.ConsoleInput()
        speak = output.ConsoleOutput()
        gavy = Gavy(listen, speak)
        gavy.query()
    elif args.speech:
        listen = listen.SpeechInput()
        with output.GTTSOutput() as speak:
            gavy = Gavy(listen, speak)
            gavy.query()
