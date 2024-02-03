#import selenium web driver
from selenium import webdriver
#import chrome driver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
#import explicit wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#import action chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome()


# Open the URL
driver.get("https://www.imdb.com/search/name/")
driver.maximize_window()  #maximize the browser window

try:
    driver.execute_script("window.scrollTo(0,500);") # scroll the window
# Click on the Name field
    name_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Name')]")))
    name_field.click()

# Enter name in name element
    name_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "name-text-input")))
    name_input.send_keys("Pavi")
    name_field.click() # click the name element

# Click on the Birth Date field
    birth_date_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Birth date')]")))
    birth_date_field.click()
# Enter input in birth date field
    birth_start_input = driver.find_element(By.NAME, "birth-date-start-input")
    birth_start_input.send_keys("01/03/2000")
    birth_end_input = driver.find_element(By.NAME, "birth-date-end-input")
    birth_end_input.send_keys("17/01/2024")
    birth_date_field.click() #after enter value close the dropdown

# Click on the Birthday
    birthday_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Birthday')]")))
    birthday_field.click()    # again


# Enter birthday
    birthday_input = driver.find_element(By.NAME, "birthday-input")
    birthday_input.click()
# enter value in birthday filed
    birthday_input.send_keys("01-02")
    birthday_field.click()

# Click on the Awards filed
    awards_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Awards & recognition')]")))
    awards_field.click()


 # Click on the button within the Awards section
    awards_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='awardsAccordion']//button[1]")))
    awards_button.click()
    awards_field.click()

# Wait for the page topics filed to be clickable
    page_topics_accordion = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='accordion-item-pageTopicsAccordion']")))
# Click on the Page Topics accordion using JavaScript
    driver.execute_script("arguments[0].click();", page_topics_accordion)


# Wait for the dropdown to be clickable
    page_topics_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "within-topic-dropdown")))

# Select "Quotes" from the dropdown using Selenium Select
    search = Select(page_topics_dropdown)
    search.select_by_visible_text("Quotes")
    page_topics_accordion.click()
    driver.execute_script("window.scrollTo(0,300);") # scroll the window

# Scroll to the Death Date filed
    death_date = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "//div[contains(text(),'Death date')]")))
    death_date.click()
    death_date_from_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='text-input__3312']")))
    death_date_to_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='text-input__3315']")))
# Enter death date range in death date field
    death_date_from_input.send_keys("02/01/2050")
    death_date_to_input.send_keys("05/07/2050")
    death_date.click()
# click the gender identity and select the female value and again close the dropdonn
    gender_identity=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Gender identity')]")))
    gender_identity.click()
    gender_identity_value=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@id='genderIdentityAccordion']//button[2]")))
    gender_identity.click()

    # CREDITS
    # Click on the Credits field
    credits_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//label[@for='accordion-item-filmographyAccordion']//span[@class='ipc-accordion_item_chevron']//*[name()='svg']"))
    )
    credits_field.click()

    # Wait for the input field to be clickable
    credits_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))).click

    # Send keys to the input field
    credits_input.send_keys("good")

except Exception as E:
    print(E)
finally:
    time.sleep(10)
    driver.quit()
