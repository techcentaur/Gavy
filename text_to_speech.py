# import pyttsx3


# def say_gavy(str):
#     engine = pyttsx3.init()
#     engine.say(str)
#     engine.runAndWait()



from pygame import mixer
from gtts import gTTS
import time
import os

def say_gavy(text):
	tts = gTTS(text=text, lang='en')
	mixer.init()
	tts.save('temp.mp3')


	with open('temp.mp3') as f:
		mixer.music.load('temp.mp3')
		mixer.music.play()
		
	os.remove('temp.mp3')
