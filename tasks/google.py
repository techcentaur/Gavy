import time
from selenium import webdriver



def search(driver, query, inp, opt):
    driver.get('http://www.google.com')
    search = browser.find_element_by_xpath('//*[@id="lst-ib"]')
    search.send_keys(query)
    search.send_keys(Keys.RETURN)
