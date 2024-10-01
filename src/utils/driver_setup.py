# /utils/driver_setup.py
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

class DriverSetup:
    def __init__(self, headless=True):
        self.options = Options()
        self.options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'  # Optional
        if headless:
            self.options.add_argument("--headless")  # Headless mode

    def get_driver(self):
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=self.options)
        return driver
