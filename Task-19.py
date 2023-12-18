#import the webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
#Give the path from which the chrome driver present
chrome_driver_path = r"C:\\Users\91637\Desktop\Selenium\chromedriver.exe"
chrome_service = ChromeService(chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://www.saucedemo.com/")
time.sleep(10)

# Question-1
# Get the url of the web page
url=driver.current_url
print(f"Current url of the page:{url}")

# Question-2
# Get the title of the web page
tit=driver.title
print(f"Current title of the page:{tit}")

# find the element using id and pass the values using send keys

from selenium.webdriver.common.by import By
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

# Question-3
# Storing the page content in the variable name called element
element = driver.find_element(By.XPATH, "//*[@id='inventory_container']")

# Get the text content of the element
page_content = element.text

# Open the file in 'w' mode to write text data
file_ = open('webpage_task_11.txt', 'w', encoding='utf-8')

# Write the text content to the file
file_.write(page_content)

# Closing the file
file_.close()

# Closing the driver
driver.close()
