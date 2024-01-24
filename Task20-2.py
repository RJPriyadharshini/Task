#### TASK20-2 #### 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import os

# Creating a function
def monthly_progress_report_download():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open the URL
    driver.get("https://labour.gov.in/")
    act = ActionChains(driver)

    # Click the button to close the popup
    driver.find_element(By.XPATH, "//button[normalize-space()='X']").click()

    # Hover over the "Documents" link using actionchains
    document = driver.find_element(By.XPATH, "//a[normalize-space()='Documents']")
    act.move_to_element(document).perform()

    # Wait for the "Monthly Progress Report" link to be clickable
    monthly = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Monthly Progress Report']")))
    monthly.click()

    # Wait for the "Download" link to be clickable
    download = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Download(227.11 KB)']")))
    download.click()

    # Switch to the alert and accept it
    alt_window = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alt_window.accept()

    # Switch to the new window
    window_id = driver.window_handles
    driver.switch_to.window(window_id[1])

    # Wait for the page to load
    time.sleep(5)

    # Creating a folder
    folder_name = "Progress report"
    folder_path = os.path.join(os.getcwd(), folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Capture the screenshot
    screenshot_path = os.path.join(folder_path, f"Report.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved of report: {screenshot_path}")
    driver.quit()

# Call the function
monthly_progress_report_download()
















