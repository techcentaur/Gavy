import tasks
import speech_to_text,text_to_speech

def main(action,task):

	verb={'open':['github','instagram','gmail','reddit','facebook'], 'play':['youtube'], 'google':['google']}
	
	for i in range(0,len(action),2):
		for j in verb[action[i]]:
			if j==action[i+1]:
				_call(action[i],j,task)

def _call(i,j,task):

	if i=='open':
		if j=='github':
			tasks.github.call()
		elif j=='instagram':
			pass
		elif j=='gmail':
			pass
		elif j=='reddit':
			tasks.reddit.call()
		elif j=='facebook':
			pass
		else:
			text_to_speech.say_gavy("Sorry sir! I didn't understand what you said!")
	elif i=='play':
		if j=='youtube':
			tasks.youtube.call(task)

		