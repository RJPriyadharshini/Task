#import selenium webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = r"C:\\Users\91637\Desktop\Selenium\chromedriver.exe"
#create webdriver object
chrome_service = ChromeService(chrome_driver_path)
driver = WebDriver(service=chrome_service)
instagram_url="https://www.instagram.com/guviofficial/"

# Open the Instagram profile
driver.get(instagram_url)
time.sleep(3)
# using XPATH finding the element
following_count =driver.find_element(By.XPATH,"//header[@class='x1qjc9v5 x78zum5 x1q0g3np x2lah0s x1n2onr6 x1qsaojo xc2v4qs x1xl8k2i x1ez9qw7 x1kcpa7z']//li[3]//button[1]")
following = following_count.text
#print the following count
print(f"Following: {following}")
time.sleep(3)
# using XPATH finding the element
follower_count =driver.find_element(By.XPATH,"//header[@class='x1qjc9v5 x78zum5 x1q0g3np x2lah0s x1n2onr6 x1qsaojo xc2v4qs x1xl8k2i x1ez9qw7 x1kcpa7z']//li[2]//button[1]")
followers = follower_count.text
#print the followers count
print(f"Followers: {followers}")


