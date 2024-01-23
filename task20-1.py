###############Task-20- question-1

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import time

# ChromeDriver path
chrome_driver_path = r"C:\\Users\91637\Desktop\Selenium\chromedriver.exe"
chrome_service = ChromeService(chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)

def navigate_and_handle_windows(url):
    driver.get(url)
    time.sleep(3)

    # Function to open a link and print its window ID
    def open_link(link_text):
        link = driver.find_element(By.XPATH, f"//a[normalize-space()='{link_text}']")
        link.click()  #perform click action
        time.sleep(1)

    # Open FAQ and Partners in new tabs
    open_link("FAQ")
    open_link("Partners")

    # Get window handles
    window_ids = driver.window_handles
    print(f"Main window ID: {window_ids[0]}")

    # Print window IDs and close the FAQ and Partners tabs
    for window_id in window_ids[1:]:
        driver.switch_to.window(window_id)
        print(f"Opened tab ID: {window_id}")
        driver.close()

    # Switch back to the main window
    driver.switch_to.window(window_ids[0])

# Navigate to the website and handle windows
navigate_and_handle_windows("https://www.cowin.gov.in")

# Add a small delay for finding the element
time.sleep(3)

# Close the browser
driver.quit()
