import nltk
import googleSearch
import analysing_input
import speechToText
from google import search
import pyttsx3

global name
global user

def inputdata(name, user):
    sayGavy("How can I help you?")
    inp = speechToText.getaudio()
    inp=inp.lower()
    task_performing(name,user,inp)

def task_performing(name,user,inp):
    inp = analysing_input.removeString(inp,"hey "+name)
    tokens=nltk.word_tokenize(inp)
    p_tags = nltk.pos_tag(tokens)
    flag=0
    if tokens[0]=="google":
        inp=analysing_input.removeString(inp,"google")
        google_search(inp)
    else:
        for (w,t) in p_tags:
            if t=="VB":
                flag=1
                break
            else:
                flag=0
        if flag==1:
            analysing_input.analyse_task(name, user, p_tags, inp)
        else:
            analysing_input.sayItagain(name,user)

def google_search(str):
    sayGavy("you want me to open it in Browser or display in terminal?")
    inp = speechToText.getaudio()
    if inp.lower()=="browser":
        googleSearch.searchInBrowser(str)
    elif inp.lower()=="terminal":
        for url in google.search(str,tld='com',lang='en',start=0,stop=10,pause=2.0):
            print(url)

def sayGavy(str):
    engine = pyttsx3.init()
    engine.say(str)
    engine.runAndWait()

def mainFile():
    user="Ankit"
    name="Jarvis"
    sayGavy("Hi Sir! Nice to meet you.")
    sayGavy("Are you " + user + " ?")
    us = speechToText.getaudio()
    if (us.lower()=="no" or us.lower()=="nope" or us.lower()=="na"):
        sayGavy("Can you please tell me who you are? If not Jessie J(Sorry for the joke)")
        user = speechToText.getaudio()
        sayGavy("Hi! "+user)
    else:
        sayGavy("Hi! "+user+" sir")
    sayGavy("My name is " + name + ". Do you want to give me a new name for this session?")
    inp = speechToText.getaudio()
    if(inp.lower()=="yes"):
        sayGavy("What should my name be?")
        name = speechToText.getaudio()
        sayGavy("so, for this session I am "+name)
    inputdata(name,user)


if __name__=="__main__":
    mainFile()