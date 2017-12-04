import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def searchInBrowser(str):
    browser = webdriver.Firefox()
    browser.get('http://www.google.com')
    search = browser.find_element_by_name('q')
    search.send_keys(str)
    search.send_keys(Keys.RETURN) # hit return after you enter search text

def searchByLink(link):
    browser = webdriver.Firefox()
    browser.get(link)