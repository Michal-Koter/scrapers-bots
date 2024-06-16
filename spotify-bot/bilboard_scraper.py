import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup


class BillboardScraper:
    def __init__(self):
        self.URL = "https://www.billboard.com/charts/hot-100"

    def get_hot_songs(self, date: str) -> list:
        """Retrieves a list of hot songs for the given date from a specified URL.

        This method checks if the provided date is in the correct format (YYYY-MM-DD)
        and is a date in the past. It then makes an HTTP request to fetch the data for
        that date, parses the HTML to extract song names, and returns them in a list.

        Args:
            date (str): A date string in the format 'YYYY-MM-DD' representing the target date
                        to fetch hot songs.

        Returns:
            list: A list of song names retrieved for the specified date.

        Raises:
            ValueError: If the date format is invalid or if the date is in the future.
            HTTPError: If the HTTP request to fetch data fails.
        """
        match = re.search(r"^\d{4}-\d{2}-\d{2}$", date)

        if match is None:
            raise ValueError("Invalid date format")

        if datetime.strptime(date, "%Y-%m-%d") > datetime.now():
            raise ValueError("Invalid date, date must be in the past")

        response = requests.get(f"{self.URL}/{date}")
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        content = soup.find("div", class_="pmc-paywall")
        songs_spans = content.select("li ul li h3")
        return [song.getText().strip() for song in songs_spans]
