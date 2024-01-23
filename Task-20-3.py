####################################task-20-3
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

# Create a folder name called  "my_screenshots"
folder_name = "my_screenshots"
folder_path = os.path.join(os.getcwd(), folder_name)
os.makedirs(folder_path, exist_ok=True)

class Photo_gallery():
    def image(self,image_xpaths):
      driver = webdriver.Chrome()

    # Open the URL
      driver.get("https://labour.gov.in/")
      driver.maximize_window()
      driver.implicitly_wait(5)
      act = ActionChains(driver)
      # Remove the add
      driver.find_element(By.XPATH, "//button[normalize-space()='X']").click()
      # Find the menu
      menu = driver.find_element(By.XPATH, "//*[@id='nav']/li[10]/a")
      # Using actionchains to perform the action
      act.move_to_element(menu).perform()
      # Find the photo gallery
      photo = driver.find_element(By.XPATH, "//a[contains(text(),'Photo Gallery')]")
      WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Photo Gallery')]"))).click()
      time.sleep(2)
      # Wait for the photo gallery page to load
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tr[@class='row-1']")))

      try:
            for i, image_xpath in enumerate(image_xpaths, start=1):
             image = driver.find_element(By.XPATH, image_xpath)
             image.click()
             time.sleep(2)
             screenshot_path = os.path.join(folder_path, f"image_{i}.png")
             driver.save_screenshot(screenshot_path)
             print(f"Screenshot saved: {screenshot_path}")
             driver.back()

      except Exception as e:
             print(f"Error: {e}")

      finally:
        time.sleep(10)
        driver.quit()

# Create an instance of the PhotoGallery class
gallery = Photo_gallery()

# Call the image method and passs the parameters for image_xpaths
gallery.image(image_xpaths=[
    "//a[normalize-space()='LEMM']","//a[normalize-space()='Swachhata Hi Seva']","//a[normalize-space()='4th EWG']",
    "//a[normalize-space()='3rd EWG']","//a[normalize-space()='2nd EWG']","//a[normalize-space()='G20']",

    "//a[contains(text(),'States/UTs Labour Secretaries Meeting, Agra from 2')]",
    "//a[normalize-space()='Mission Mode Recruitment']",
    "//a[contains(text(),'Special Day to observe the one-day Countdown to th')]","//img[@title='International Labour Conference']"
])

