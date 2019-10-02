import urllib.error
from classes.InputConverter import InputConverter
from classes.LyricScraper import LyricScraper

def main():
    artist = input("Enter an artist or band name: ")
    if artist.lower() == 'q':
        return

    song = input("Enter a song name from the artist or band: ")
    if song.lower() == 'q':
        return

    converter = InputConverter(artist, song)

    artist = converter.convertToArtistString()
    song = converter.convertToSongString()

    url = converter.createURL(artist, song)
    try:
        page = converter.readURL(url)
    except urllib.error.HTTPError:
        print("ERROR: Could not return lyrics! (Try retyping your artist or song.)")
        main()

    scraper = LyricScraper(page)
    artist_name = scraper.getArtistName()
    song_name = scraper.getSongName()
    feature_name = scraper.getFeatureName()
    lyrics = scraper.getLyrics()

    if feature_name != None:
        print("\n" + song_name, "-", artist_name, feature_name.get_text() + "\n")
    else:
        print("\n" + song_name, "-", artist_name + "\n")
    print(lyrics)
    main()

main()