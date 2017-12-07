

def positive(response):
	yes = ['yes', 'yeah', 'yea', 'haan', 'yo', 'yep']
	no = ['no', 'nah', 'nope', 'na']

	for y in yes:
		if y in response:
			return True

	for n in no:
		if n in response:
			return False

	return False
