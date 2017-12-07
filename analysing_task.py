import nltk

import work_data
import main_process
import speech_to_text
import tasks


def analyse_task(name,user,p_tags,inp):
    
    verb="null"
    for (w,t) in p_tags:
        if t=="VB":
            verb=w
    if verb!="null":
        if verb in work_data.verb_data:
            verb_analyse(verb,inp)
    else:
        say_it_again(name,user)

def say_it_again(name,user):
    
    main_process.say_gavy("Sorry sir! I didn't quite understand what you said? Can you please say it again")
    main_process.input_data(name, user)


def remove_string(str,str_toberemoved):
    if str_toberemoved in str:
        str=str.replace(str_toberemoved,"",1)
    return str


def verb_analyse(verb,inpStr):
    if(verb.lower()=="play"):
        inpStr=remove_string(inpStr,"play")
        inpStrTag = nltk.pos_tag(inpStr)
        strdict={}
        for (w,t) in inpStrTag:
            strdict[w]=t
        j=0
        for i in range(0,len(inpStr)):
            if inpStr[i].lower()=="youtube":
                j=i
                break
        if inpStrTag[j-1][1]=="IN":
            inpStr=remove_string(inpStr,inpStrTag[j-1][0]+"youtube")

        tasks.youtube.play(inpStr)
    elif(verb.lower()=="open"):
        if "github" in inpStr:
            say_gavy("Do you want me to open github in Incongnito mode?")
            ask_Mode=speech_to_text.getaudio()
            if(ask_Mode.lower()=="yes"):
                say_gavy("Please enter your credentials!")
                u=input("username: ")
                p=input("password: ")
                github.incognito(u,p)
            else:
                github.normal_mode()