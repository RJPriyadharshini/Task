from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

import pytest


@pytest.fixture()
def driver():
    chrome_service = ChromeService(r"C:\\Users\91637\Desktop\Selenium\chromedriver.exe")
    driver = webdriver.Chrome(service=chrome_service)
    driver.maximize_window()
    yield driver
