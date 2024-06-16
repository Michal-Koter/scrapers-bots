from bilboard_scraper import BillboardScraper
from spotify_client import SpotifyClient

if __name__ == '__main__':
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

    scraper = BillboardScraper()
    song_names = scraper.get_hot_songs(date)

    spotify_client = SpotifyClient()
    playlist_id = spotify_client.create_playlist(song_names, date)

    print(playlist_id)
