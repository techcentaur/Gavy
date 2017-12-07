import nltk

import speech_to_text,text_to_speech

from tasks import main
from NLPapi import main

def input_data(name, user):
    text_to_speech.say_gavy("How can I help you, Sir?")
    task_str = speech_to_text.getaudio()
    task_str=task_str.lower()
    task(name,user,task)

def task(name,user,task):
    t1=main.Main(task, name, user)
    action = t1.action_work()
    main.main(action,task)

def begin_file():
    #defaults
    user="Ankit"
    name="Gavy"

    text_to_speech.say_gavy("Hi Sir! Nice to meet you."+"Are you " + user + " ?")
    
    user_check = speech_to_text.getaudio()
    for n in ['no','nah','nope','na']:
        if n in user_check:
            text_to_speech.say_gavy("Can you please tell me who you are?")
            user = speech_to_text.getaudio()
    text_to_speech.say_gavy("Hi! "+user+" sir") 
    
    text_to_speech.say_gavy("My name is " + name +".You can call me from that name.")
    name_check = speech_to_text.getaudio()
    for y in ['yes','yeah','yea','haan']:
        if y in name_check:
            text_to_speech.say_gavy("What should my name be?")
            name = speech_to_text.getaudio()
            text_to_speech.say_gavy("so, for this session I am "+name +".")
    
    input_data(name,user)


if __name__=="__main__":
    begin_file()