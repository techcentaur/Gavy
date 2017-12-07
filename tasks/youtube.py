import urllib.request
from bs4 import BeautifulSoup
import selenium
import speech_to_text,text_to_speech

def play(str):
    textToSearch = str
    query = urllib.request.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html,'html.parser')
    for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
        link1 = 'https://www.youtube.com' + vid['href']
        linkD = 'https://www.ssyoutube.com' + vid['href']
        break
    driver = selenium.webdriver.FireFox()
    driver.get(link1)
    text_to_speech.say_gavy("Should I download the song?")
    ask_dwnld = speech_to_text.getaudio()
    
    if "yes" in ask_dwnld.lower():
        download(linkD,driver)


def download(str):
    driver.get(str)
    webdriver.find_element_by_css_selector('.link.link-download.subname ga_track_events.download-icon').click()
    text_to_speech.say_gavy("The Downloading is started! Sir")

def call(str):
    
    if "play" in str:
        str=str.replace("play ","")
    if "the song" in str:
        str=str.replace("the song ","")
    if "in youtube" in str:
        str=str.replace("in youtube","")

    play(str)