from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class FormsBot:
    """
    A class to automate the submission of forms using Selenium.

    Attributes:
        driver (webdriver.Chrome): The WebDriver instance used to interact with the web browser.
        url (str): The URL of the form page to be automated.
    """
    def __init__(self, url: str):
        """
        Initializes the FormsBot with the specified URL.

        Args:
            url (str): The URL of the form page to be automated.
        """
        self.driver = webdriver.Chrome()
        self.url = url

    def send_form(self, address: str, price: str, link: str) -> None:
        """
        Fills in the form fields with the provided address, price, and link values,
        and submits the form.

        Parameters:
            address (str): The address to be entered into the form.
            price (str): The price to be entered into the form.
            link (str): The link to be entered into the form.
        """
        self.driver.get(self.url)
        sleep(2)

        address_input = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_input = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        submit = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div')

        address_input.send_keys(address)
        price_input.send_keys(price)
        link_input.send_keys(link)
        submit.click()