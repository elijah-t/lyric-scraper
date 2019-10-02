import urllib.request
import re

class InputConverter:
    def __init__(self, artist, song):
        self.artist = artist
        self.song = song

    def convertToArtistString(self):
        if self.artist[0:4].lower() == "the ":
            return re.sub("[^A-Za-z0-9]+", "", self.artist).lower()[3:len(self.artist)]
        return re.sub("[^A-Za-z0-9]+", "", self.artist).lower()

    def convertToSongString(self):
        return re.sub("[^A-Za-z0-9]+", "", self.song).lower()

    def createURL(self, artist, song):
        return "http://www.azlyrics.com/lyrics/" + artist + "/" + song + ".html"

    def readURL(self, url):
        return urllib.request.urlopen(url).read()

    def getArtist(self):
        return self.artist

    def getSong(self):
        return self.song

    def setArtist(self, artist):
        self.artist = artist
    
    def setSong(self, song):
        self.song = song