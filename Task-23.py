#DRAG AND DROP
import time
#import selenium webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
#import action chains
from selenium.webdriver.common.action_chains import ActionChains
#create webdriver object
driver = webdriver.Chrome()
#open the url
driver.get("https://jqueryui.com/droppable/")
frame_id=driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
# Switched to frame
driver.switch_to.frame(frame_id)
#get source element
source_element = driver.find_element(By.XPATH, "//div[@id='draggable']")
#get target element
target_element = driver.find_element(By.XPATH, "//div[@id='droppable']")
#create action chain object and stored in one variable
act = ActionChains(driver)
# perform the action
act.drag_and_drop(source_element, target_element).perform()
time.sleep(10)
driver.quit()
