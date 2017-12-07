

def open():
	driver = selenium.webdriver.Firefox()
	driver.get('https://www.reddit.com')

def login(username, password):
	driver = selenium.webdriver.Firefox()
	driver.get('https://www.reddit.com')
	username = driver.find_element_by_name('user')
	username.send_keys(username)
	driver.find_element_by_name('passwd').send_keys(password)
	driver.find_element_by_name('rem').click()
	username.submit()

def call():
	text_to_speech.say_gavy("It looks like, This site needs credentials for login. Do you want to enter username and password?")
    ch = speech_to_text.getaudio()
    if "yes" in ch or "yeah" in ch:
        text_to_speech.say_gavy("Enter your credentials-")
        username = input("username :")
        password = input("password :")
        login(username,password)
    else:
    	text_to_speech.say_gavy("Opening reddit.com")
    	open()
