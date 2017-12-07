import selenium
import helper

    

def login(driver, username, password):
    driver.get('http://www.github.com/login')
    driver.find_element_by_id("login_field").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_name("commit").click()


def open(driver, inp, opt):
    driver.get('https://www.github.com')

    opt.output('Do you want to login to Github?')
    response = inp.input()
    if helper.positive(response):
        username = input('[?] Github username : ')
        password = input('[?] Github password : ')
        login(driver, username,password)
