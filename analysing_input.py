import nltk
import work_data
import youtubeSongPD
import githubThrough
import text_process

def analyse_task(name,user,p_tags,inp):
    temp_verbs=[]
    for (w,t) in p_tags:
        if t=="VB":
            temp_verbs.append(w)
    if len(temp_verbs)!=0:
        for i in temp_verbs:
            if i in work_data.verbData:
                verb_analyse(i,inp)
                break
    else:
        sayItagain(name,user)
    text_process.inputdata(name,user)

def sayItagain(name,user):
    print("Sorry sir! I didn't quite understand what you said? Can you please say it again")
    text_process.inputdata(name, user)


def removeString(str,str_toberemoved):
    if str_toberemoved in str:
        str=str.replace(str_toberemoved,"",1)
    return str


def verb_analyse(verb,inpStr):
    if(verb.lower()=="play"):
        inpStr=removeString(inpStr,"play")
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
            inpStr=removeString(inpStr,inpStrTag[j-1][0]+"youtube")

        youtubeSongPD.play(inpStr)
    elif(verb.lower()=="open"):
        if "github" in inpStr:
            ask_Mode=input("Do you want me to open github in Incongnito mode?")
            if(ask_Mode.lower()=="yes"):
                print("Please enter your credentials!")
                u=input("username: ")
                p=input("password: ")
                githubThrough.incognito(u,p)
            else:
                githubThrough.normal_mode()