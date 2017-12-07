import selenium


def incognito(u,p):
    firefox_profile = selenium.webdriver.FirefoxProfile()
    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
    driver = selenium.webdriver.Firefox(firefox_profile=firefox_profile)
    driver.get('http://www.github.com/login')
    username = driver.find_element_by_id("login_field")
    password = driver.find_element_by_id("password")
    username.send_keys(u)
    password.send_keys(p)
    driver.find_element_by_name("commit").click()


def normal_mode():
    profile = selenium.webdriver.FirefoxProfile()
    profile.set_preference('media.navigator.permission.disabled', True)
    profile.update_preferences()
    firefox = selenium.webdriver.Firefox(firefox_profile=profile)
    firefox.get('https://www.github.com')

def call():
    text_to_speech.say_gavy("do you want to open it in normal mode or incognito mode?")
    mode = speech_to_text.getaudio()
    if "normal" in mode:
        normal_mode()
    else:
        text_to_speech.say_gavy("I need credentials for login in github? Do you want to enter them?")
        ch = speech_to_text.getaudio()
        if "yes" in ch or "yeah" in ch:
            username = input("username :")
            password = input("password :")
            incognito(username,password)