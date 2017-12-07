import pyttsx3

def func():
	engine = pyttsx3.init()
	rate = engine.getProperty('rate')
	engine.setProperty('rate', rate+100)
	engine.setProperty('voice', 'english')
	engine.say("Ankit Sir!")
	engine.runAndWait()
	engine.stop()


if __name__=="__main__":
	func()