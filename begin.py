import nltk
import pyttsx3

import analysing_task
import speech_to_text

import tasks
from NLPapi import main

def input_data(name, user):
    say_gavy("How can I help you, Sir?")
    task_str = speech_to_text.getaudio()
    task_str=task_str.lower()
    task(name,user,task)

def task(name,user,task):
    t1=main.Main(task)

def say_gavy(str):
    engine = pyttsx3.init()
    engine.say(str)
    engine.runAndWait()

def begin_file():
    #defaults
    user="Ankit"
    name="Gavy"

    say_gavy("Hi Sir! Nice to meet you."+"Are you " + user + " ?")
    
    user_check = speech_to_text.getaudio()
    for n in ['no','nah','nope','na']:
        if n in user_check:
            say_gavy("Can you please tell me who you are?")
            user = speech_to_text.getaudio()
    say_gavy("Hi! "+user+" sir") 
    
    say_gavy("My name is " + name +".You can call me from that name.")
    name_check = speech_to_text.getaudio()
    for y in ['yes','yeah','yea','haan']:
        if y in name_check:
            say_gavy("What should my name be?")
            name = speech_to_text.getaudio()
            say_gavy("so, for this session I am "+name +".")
    
    input_data(name,user)


if __name__=="__main__":
    begin_file()