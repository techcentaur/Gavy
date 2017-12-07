import pyttsx3
from pygame import mixer
from gtts import gTTS
import time
import os



class Output:
    def __init__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def output(self, message):
        pass


class ConsoleOutput(Output):
    def __init__(self):
        pass

    def output(self, message):
        print('[*] {}'.format(message))


class PyTTSOutput(Output):
    def __init__(self):
        self.engine = pyttsx3.init()

    def output(self, message):
        self.engine.say(message)
        self.engine.runAndWait()


class GTTSOutput(Output):
    def __init__(self):
        mixer.init()
        self.tempfile = None
        self.tempname = 'speech.mp3.temp'
    
    def __enter__(self):
        self.tempfile = open(self.tempname, 'wb')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.tempfile.close()
        os.remove(self.tempname)

    def output(self, message):
        tts = gTTS(text=message, lang='en')
        
        if not self.tempfile:
            tts.save(self.tempname)
            self.playmixer()
            os.remove(self.tempname)
        else:
            self.tempfile.truncate()
            tts.write_to_fp(self.tempfile)
            self.playmixer()

    def playmixer(self):
        mixer.music.load(self.tempname)
        mixer.music.play()
        while mixer.music.get_busy():
            pass


with GTTSOutput() as o:
    o.output('This is console')
