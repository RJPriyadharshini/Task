import pytest
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

txtName_xpath="//div[contains(text(),'Name')]"
txtNameid_value="name-text-input"
txtbirth_xpath="//div[contains(text(),'Birth date')]"
namebirth_start_input="birth-date-start-input"
namebirth_end_input="birth-date-end-input"
txtbirthday_xpath="//div[contains(text(),'Birthday')]"
txtbirthday_XPATH="//input[@id='text-input__13']"
txtawards_xpath="//div[contains(text(),'Awards & recognition')]"
buttonawards_xpath="//div[@id='awardsAccordion']//button[1]"
txtpage_xpath="//label[@for='accordion-item-pageTopicsAccordion']"
txtpagevalue_name="within-topic-dropdown"
txtgender_xpath="//div[contains(text(),'Gender identity')]"
buttongender_xpath="//div[@id='genderIdentityAccordion']//button[2]"

class InputFieldPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.execute_script("window.scrollTo(0,500);")

    def SetNameInput(self, name):
        wait = WebDriverWait(self.driver, 20)
        # Scroll to the element
        namefield = wait.until(EC.visibility_of_element_located((By.XPATH, txtName_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView();", namefield)
        namefield.click()
        # Wait for the input field to be visible and enter the name
        name_input = wait.until(EC.visibility_of_element_located((By.NAME, txtNameid_value)))
        name_input.send_keys(name)

    def SetBirthDate(self, start_date, end_date):
        wait = WebDriverWait(self.driver, 30)
        birth_date_field = wait.until(EC.visibility_of_element_located((By.XPATH, txtbirth_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView();", birth_date_field)
        birth_date_field.click()
        birth_start_input = wait.until(EC.element_to_be_clickable((By.NAME, namebirth_start_input)))
        birth_start_input.send_keys(start_date)
        birth_end_input = wait.until(EC.element_to_be_clickable((By.NAME, namebirth_end_input)))
        birth_end_input.send_keys(end_date)
    def SetBirthday(self,birthday):
        wait = WebDriverWait(self.driver, 10)
        birthday_field = wait.until(EC.visibility_of_element_located((By.XPATH, txtbirthday_xpath)))
        birthday_field.click()
        birthday_input = wait.until(EC.element_to_be_clickable((By.XPATH, txtbirthday_XPATH)))
        birthday_input.send_keys(birthday)
    def SelectAwards(self):
        wait = WebDriverWait(self.driver, 10)
        awards_button = wait.until(EC.visibility_of_element_located((By.XPATH, txtawards_xpath)))
        awards_button.click()
        awards_dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, buttonawards_xpath)))
        awards_dropdown.click()
    def SelectPageTopic(self):
        wait = WebDriverWait(self.driver, 10)
        pagetopic_button = wait.until(EC.visibility_of_element_located((By.XPATH, txtpage_xpath)))
        pagetopic_button.click()
        page_value = wait.until(EC.visibility_of_element_located((By.NAME, txtpagevalue_name)))
        page_value.click()
    def SelectGender(self):
        wait = WebDriverWait(self.driver, 10)
        gender_button = wait.until(EC.visibility_of_element_located((By.XPATH, txtgender_xpath)))
        gender_button.click()
        gender_value = wait.until(EC.visibility_of_element_located((By.XPATH, buttongender_xpath)))
        gender_value.click()


