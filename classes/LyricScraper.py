from bs4 import BeautifulSoup

class LyricScraper:
    def __init__(self, page):
        self.page = BeautifulSoup(page, "html.parser")

    def getArtistName(self):
        temp = self.page.select_one("body > div.container.main-page > div > div.col-xs-12.col-lg-8.text-center > div.lyricsh > h2 > b").get_text()
        return ' '.join(temp.split(' ')[:-1])

    def getSongName(self):
        return self.page.select_one("body > div.container.main-page > div > div.col-xs-12.col-lg-8.text-center > b").get_text().strip('\"')

    def getFeatureName(self):
        return self.page.select_one("body > div.container.main-page > div > div.col-xs-12.col-lg-8.text-center > span")

    def getLyrics(self):
        return self.page.find_all('div')[21].text.strip()