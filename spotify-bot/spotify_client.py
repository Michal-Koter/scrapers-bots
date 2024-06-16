import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = os.environ.get('SPOTIFY_REDIRECT_URI')


class SpotifyClient:
    def __init__(self):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                redirect_uri=REDIRECT_URI,
                scope="playlist-modify-private",
                show_dialog=True,
            )
        )

        self.user_id = self.sp.current_user()["id"]

    def create_playlist(self, song_names: list, date: str) -> str:
        """Create spotify playlist with given songs and date.

        This method searches for each song in the provided list within the specified year,
        extracts the song URIs, and creates a private playlist on Spotify. It then adds
        the songs to the newly created playlist and returns the playlist ID.

        Args:
            song_names (list): A list of song names to be added to the playlist.
            date (str): A date string in the format 'YYYY-MM-DD' which is used to search
                        for songs within that year.

        Returns:
            str: The ID of the created playlist.

        Notes:
            - If a song is not found on Spotify, it is skipped, and a message is printed.
        """
        song_uris = []
        year = date.split("-")[0]
        for song in song_names:
            result = self.sp.search(q=f"track:{song} year:{year}", type="track")
            print(result)
            try:
                uri = result["tracks"]["items"][0]["uri"]
                song_uris.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")

        playlist = self.sp.user_playlist_create(user=self.user_id, name=f"{date} Billboard 100", public=False)

        self.sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

        return playlist["id"]
