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
