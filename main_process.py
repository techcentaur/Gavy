import nltk
import pyttsx3

import analysing_task
import speech_to_text
import tasks

def inputdata(name, user):
    say_gavy("How can I help you?")
    task = speechToText.getaudio()
    task=task.lower()
    task(name,user,task)

def task(name,user,task):
    task = analysing_input.removeString(task,"hey "+name)
    
    pos_tags = nltk.pos_tag(nltk.word_tokenize(task))
    verb_flag=0
    if word_tokenize(task)[0]=="google":
        string=analysing_input.removeString(inp,"google")
        task.google.(string)
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
    
    say_gavy("you want me to open it in Browser or display in terminal?")
    
    open_choice = speechToText.getaudio()
    for ch in ['browser','chrome','firefox']:
        if ch in open_choice.lower():
            tasks.google.search_in_browser(str)
    else:
        for url in google.search(str,tld='com',lang='en',start=0,stop=10,pause=2.0):
            print(url)

def say_gavy(str):
    engine = pyttsx3.init()
    engine.say(str)
    engine.runAndWait()

def main_ile():
    #defaults
    user="Ankit"
    name="Jarvis"

    say_gavy("Hi Sir! Nice to meet you.")
    say_gavy("Are you " + user + " ?")
    
    user_check = speechToText.getaudio()
    for n in ['no','nah','nope','na']:
        if n in user_check.lower()
            say_gavy("Can you please tell me who you are?")
            user = speechToText.getaudio()
            say_gavy("Hi! "+user)
        else:
            say_gavy("Hi! "+user+" sir") 
    say_gavy("My name is " + name + ". Do you want to give me a new name for this session?")
    name_check = speechToText.getaudio()
    for y in ['yes','yeah','yea','haan']:
        if y in name_check.lower():
            say_gavy("What should my name be?")
            name = speechToText.getaudio()
            say_gavy("so, for this session I am "+name ".")
    
    input_data(name,user)


if __name__=="__main__":
    main_file()