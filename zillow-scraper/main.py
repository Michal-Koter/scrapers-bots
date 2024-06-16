from forms_bot import FormsBot
from zillow_scraper import ZillowScraper

ZILLOW_URL = "https://www.zillow.com"
SEARCH_PARAMS = "san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-122.53477961341001%2C%22east%22%3A-122.33393580237485%2C%22south%22%3A37.71434481496411%2C%22north%22%3A37.82073254998473%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A593908%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D"
FORM_URL = "YOUR_FORM_URL"

if __name__ == "__main__":
    scraper = ZillowScraper(ZILLOW_URL, SEARCH_PARAMS)

    links = scraper.get_properties_links()
    print(f"There are {len(links)} links to individual listings in total: \n")
    print(links)

    prices = scraper.get_prices()
    print(f"\n After having been cleaned up, the {len(prices)} prices now look like this: \n")
    print(prices)

    addresses = scraper.get_addresses()
    print(f"\n After having been cleaned up, the {len(addresses)} addresses now look like this: \n")
    print(addresses)

    bot = FormsBot(FORM_URL)
    for link, price, address in zip(links, prices, addresses):
        bot.send_form(address, price, link)
