import pytest
from selenium import webdriver

URL = "https://www.imdb.com/search/name/"

@pytest.fixture(scope="module")  #fixture will be executed once per module.
def browser():
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()