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

# get the url of the web page
r=driver.current_url
print(r)

#get the title of the web page
a=driver.title
print(a)
# find the element using id and enter the values using send keys
from selenium.webdriver.common.by import By
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()


# Storing the page source in page variable
page = driver.page_source.encode('utf-8')
# print(page)

# # Open a webpage_task_11.txt file in 'wb' mode to write binary data
file_ = open('webpage_task_11.txt', 'wb')

# Write the entire page content
file_.write(page)

# Closing the file
file_.close()

# Closing the driver
driver.close()