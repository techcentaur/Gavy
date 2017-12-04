import selenium

def incognito(u,p):
    firefox_profile = selenium.webdriver.FirefoxProfile()
    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
    driver = selenium.webdriver.Firefox(firefox_profile=firefox_profile)
    driver.get('http://www.github.com/login')
    username = selenium.find_element_by_id("login_field")
    password = selenium.find_element_by_id("password")
    username.send_keys(u)
    password.send_keys(p)
    selenium.find_element_by_name("commit").click()

def normal_mode():
    browser = webdriver.Firefox()
    browser.get('http://www.github.com')