import urllib.request
from bs4 import BeautifulSoup
import selenium


class YouTube:
    def __init__(self, driver, inp, opt, query):
        response = requests.get('https://www.youtube.com/results', params={'search_query': query})
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        video = soup.findAll(attrs={'class': 'yt-uix-tile-link'})[0]
        self.id = video['href'][8:]
        self.driver = driver

    def __clean(query):
        garbage = ['play ', 'the song ', 'in youtube']
        for g in garbage:
            query = query.replace(g, '')
        
        return query

    def play(self):
        self.driver.get('https://www.youtube.com/watch?v=' + self.id)
        self.opt.output('Should I download the song?')
        ifd = self.inp.input()

        if helper.positive(ifd):
            download()

    def download(self):
        self.driver.get('https://www.ssyoutube.com/watch?v=' + self.id)
        self.driver.find_element_by_css_selector('.link.link-download.subname ga_track_events.download-icon').click()
        self.opt.output('The downloading has started.')
