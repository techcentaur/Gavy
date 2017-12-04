import requests
from bs4 import BeautifulSoup
# import speechToText
# from text_process import sayGavy


class YouTube:
    def __init__(self, query, driver):
        response = requests.get('https://www.youtube.com/results', params={'search_query': query})
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        video = soup.findAll(attrs={'class': 'yt-uix-tile-link'})[0]
        self.id = video['href'][8:]
        self.driver = driver

    def play(self):    
        self.driver.get('https://www.youtube.com/watch?v=' + self.id)

    def download(self):
        self.driver.get('https://www.ssyoutube.com/watch?v=' + self.id)
        self.driver.find_element_by_css_selector('.link.link-download.subname ga_track_events.download-icon').click()
        # sayGavy("The Downloading is started! Sir")


# sayGavy("Should I download the song?")
#         ask_dwnld = speechToText.getaudio()
#         if "yes" in ask_dwnld.lower():
#             download(linkD)