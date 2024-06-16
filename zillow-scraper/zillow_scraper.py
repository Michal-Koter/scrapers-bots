from bs4 import BeautifulSoup
import requests


class ZillowScraper:
    """
    A class used to scrape property listings from Zillow.

    Attributes:
        url (str): The base URL for the Zillow website.
        params (str): The URL parameters to specify the search criteria.
        header (dict): The HTTP headers used for making requests.
    """

    def __init__(self, url: str, params: str):
        """
        Initializes the ZillowScraper with the specified URL and parameters.

        Args:
            url (str): The base URL for the Zillow website.
            params (str): The URL parameters to specify the search criteria.
        """
        self.url = url
        self.params = params
        self.header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
        }

    def __get_soup(self, url: str, headers: dict) -> BeautifulSoup:
        """
        Makes a GET request to the specified URL with the provided headers and returns a BeautifulSoup object of the page content.

        Args:
            url (str): The URL to make the GET request to.
            headers (dict): The headers to include in the HTTP request.

        Returns:
            BeautifulSoup: A BeautifulSoup object containing the parsed HTML content of the page.
        """
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')

    def get_properties_links(self) -> list:
        """
        Retrieves a list of property links from the Zillow search results.

        Returns:
            list of str: A list of URLs pointing to individual property listings.
        """
        soup = self.__get_soup(self.url + "/" + self.params, self.header)
        link_elements = soup.select(
            "div.StyledPropertyCardDataWrapper-c11n-8-101-0__sc-hfbvv9-0.hHVup.property-card-data > a")

        links = []
        for link in link_elements:
            if not link["href"].startswith("https://www.zillow.com"):
                links.append("https://www.zillow.com" + link["href"])
            else:
                links.append(link["href"])

        return links

    def get_prices(self) -> list:
        """
        Retrieves a list of property prices from the Zillow search results.

        Returns:
            list of str: A list of property prices as strings.
        """
        soup = self.__get_soup(self.url + "/" + self.params, self.header)
        price_elements = soup.select("div.StyledPropertyCardDataArea-c11n-8-101-0__sc-10i1r6-0.EflFW > div > span")

        return [element.get_text(strip=True)[:6] for element in price_elements]

    def get_addresses(self) -> list:
        """
        Retrieves a list of property addresses from the Zillow search results.

        Returns:
            list of str: A list of property addresses as strings.
        """
        soup = self.__get_soup(self.url + "/" + self.params, self.header)

        address_elements = soup.find_all("address")

        return [address.get_text(strip=True).replace(" | ", " ") for address in address_elements]
