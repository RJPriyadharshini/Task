#DRAG AND DROP
import time
#import selenium webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
#import action chains
from selenium.webdriver.common.action_chains import ActionChains
#create webdriver object
driver = webdriver.Chrome()
driver.implicitly_wait(10)
#oepn the url
driver.get("https://jqueryui.com/droppable/")

# Implicit wait is applicable to all the statements below
f1=driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
# Switched to frame 1
driver.switch_to.frame(f1)
#get source element
source_element = driver.find_element(By.XPATH, "//div[@id='draggable']")
#get target element
target_element = driver.find_element(By.XPATH, "//div[@id='droppable']")
#create action chain object
act = ActionChains(driver)
#perform the action
act.drag_and_drop(source_element, target_element).perform()
time.sleep(10)
driver.quit()
