import nltk
import googleSearch
import analysing_input
import speechToText
from google import search

global name;
global user;

def inputdata(name,user):
    inp = speechToText.getaudio("How can I help you?")
    print(inp)
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
        print(flag)
        if flag==1:
            analysing_input.analyse_task(name, user, p_tags, inp)
        else:
            analysing_input.sayItagain(name,user)

def google_search(str):
    inp = speechToText.getaudio("you want me to open it in Browser or display in terminal?")
    if inp.lower()=="browser":
        googleSearch.searchInBrowser(str)
    elif inp.lower()=="terminal":
        for url in google.search(str,tld='com',lang='en',start=0,stop=10,pause=2.0):
            print(url)

def mainFile():
    user="Ankit"
    name="Jarvis"
    print("Hi Sir! Nice to meet you.")
    us = speechToText.getaudio("Are you "+user+" ?")
    if (us.lower()=="no" or us.lower()=="nope" or us.lower()=="na"):
        user = input("Can you please tell me who you are? If not Jessie J(Sorry for the joke)")
        print("Hi! "+user)
    else:
        print("Hi! "+user+" sir")
    inp = speechToText.getaudio("My name is "+name+". Do you want to give me a new name for this session?")
    if(inp.lower()=="yes"):
        name = input("What should my name be?")
        print("so, for this session I am "+name)
    inputdata(name,user)


if __name__=="__main__":
    mainFile()