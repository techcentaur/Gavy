import pyttsx3


def say_gavy(str):
    engine = pyttsx3.init()
    engine.say(str)
    engine.runAndWait()
