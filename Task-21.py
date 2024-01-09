#Task-21#

#import selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
#get cookies for before login
before_login=driver.get_cookies()
print(len(before_login))
#print the cookies in console
print(f"Cookies before login saucedemo:,{before_login}")

driver.get("https://www.saucedemo.com/")
user_name = "visual_user"
passcode = "secret_sauce"
#find element using xpath and send the values using send keys
user = driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(user_name)
password = driver.find_element(By.XPATH, "//input[@id='password']").send_keys(passcode)
Button_ = driver.find_element(By.XPATH, "//input[@id='login-button']").click()
# using below to get the cookies in after login 
after_login=driver.get_cookies()
print(len(after_login))
print(f"Cookies after login saucedemo :,{after_login}")
driver.maximize_window()
driver.implicitly_wait(10)
#again login the zen portal to get the cookies 
before_loginzen=driver.get_cookies()
print(len(before_loginzen))
print(f"Cookies before login zen:,{before_loginzen}")
driver.get("https://www.zenclass.in/login")

user = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input").send_keys("priyaramasamy2131@gmail.com")
password = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input").send_keys("Priya@07")
Button = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div[2]/div/div[1]/form/button").click()
time.sleep(10)
#log out the zen portal
Button_1= driver.find_element(By.XPATH, "//*[@id='root']/nav/div/div/div/span/img").click()
Button_2 = driver.find_element(By.XPATH, "//button[normalize-space()='Logout']").click()
#after logout to get the cookies and print the cookies in console
after_loginzen=driver.get_cookies()
print(len(after_loginzen))
print(f"Cookies after login zen:,{after_loginzen}")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(10)
#close the driver 
driver.quit()
