from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

@pytest.fixture
def browser():
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--no-sandbox")  # Example of adding an option
    
    driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
    driver.maximize_window()
    driver.get(URL)
    
    yield driver
    
    driver.quit()  # Close the browser
