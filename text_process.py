import nltk
import googleSearch
import analysing_input
from google import search

global name;
global user;

def inputdata(name,user):
    inp = input("How can I help you?")
    for w in inp:
        w = w.lower()
    task_performing(name,user,inp)

def task_performing(name,user,inp):
    inp = analysing_input.removeString(inp,"hey "+name)
    tokens=nltk.word_tokenize(inp)
    p_tags = nltk.pos_tag(tokens)
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
        print(p_tags)
        analysing_input.sayItagain(name,user)


def google_search(str):
    inp = input("you want me to open it in Browser or display in terminal?")
    for i in inp:
        if i.lower()=="browser":
            googleSearch.searchInBrowser(str)
            break
        elif i.lower()=="terminal":
            for url in google.search(str,tld='com',lang='en',start=0,stop=10,pause=2.0):
                print(url)
            break
def mainFile():
    user="Ankit"
    name="Jarvis"
    print("Hi Sir! Nice to meet you.")
    print("Are you "+user+" ?")
    us = input()
    if (us.lower()=="no" or us.lower()=="nope" or us.lower()=="na"):
        user = input("Can you please tell me who you are? If not Jessie J(Sorry for the joke)")
        print("Hi! "+user)
    print("My name is "+name+". Do you want to give me a new name for this session?")
    inp = input()
    if(inp.lower()=="yes"):
        name = input("What should my name be?")
        print("so, for this session I am "+name)
    inputdata(name,user)


if __name__=="__main__":
    mainFile()