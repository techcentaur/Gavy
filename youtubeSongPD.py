import urllib.request
from bs4 import BeautifulSoup
import googleSearch
from selenium import webdriver
import speechToText


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
    googleSearch.searchByLink(link1)
    ask_dwnld = speechToText.getaudio("Should I download the song?")
    if "yes" in ask_dwnld.lower():
        download(linkD)


def download(str):
    googleSearch.searchByLink(str)
    webdriver.find_element_by_css_selector('.link.link-download.subname ga_track_events.download-icon').click()
    print("The Downloading is started! Sir")