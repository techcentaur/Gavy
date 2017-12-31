import speech_recognition as sr



class Input:
    def input(self):
        pass


class ConsoleInput(Input):
    def input(self):
        return input('[?] ')


class SpeechInput(Input):
    def __init__(self):
        self.recog = sr.Recognizer()

    def input(self):
        with sr.Microphone() as source:
            audio = self.recog.listen(source)
        
        try:
            return self.recog.recognize_google(audio)
        except sr.UnknownValueError:
            print('[!] Could not understand the audio!')
        except sr.RequestError as e:
            print('[!] Could not request results: {0}'.format(e))
