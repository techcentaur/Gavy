import speech_recognition as sr

def getaudio():
	#get audio from microphone
	r=sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
	try:
		return r.recognize_google(audio)
	except sr.UnknownValueError:
		print("Couldnot understand the audio! Sir")
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))