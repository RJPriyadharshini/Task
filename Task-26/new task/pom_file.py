import time
from selenium.webdriver.support.ui import Select
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC

txtName_xpath="//div[contains(text(),'Name')]"
txtNameid_value="name-text-input"
txtbirth_xpath="//div[contains(text(),'Birth date')]"
namebirth_start_input="birth-date-start-input"
namebirth_end_input="birth-date-end-input"
txtbirthdayinput_xpath="//div[contains(text(),'Birthday')]"
txtbirthday_name="birthday-input"
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
        self.wait = WebDriverWait(self.driver, 20)

    def SetNameInput(self, name):
        namefield = self.wait.until(EC.visibility_of_element_located((By.XPATH, txtName_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView();", namefield)
        namefield.click()
        name_input = self.wait.until(EC.visibility_of_element_located((By.NAME, txtNameid_value)))
        name_input.send_keys(name)

    def SetBirthDate(self, start_date, end_date):
        birth_date_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, txtbirth_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView();", birth_date_field)
        birth_date_field.click()
        birth_start_input = self.wait.until(EC.element_to_be_clickable((By.NAME, namebirth_start_input)))
        birth_start_input.send_keys(start_date)
        birth_end_input = self.wait.until(EC.element_to_be_clickable((By.NAME, namebirth_end_input)))
        birth_end_input.send_keys(end_date)

    def SetBirthday(self, birthday):
        birthday_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, txtbirthdayinput_xpath)))
        birthday_field.click()
        birthday_input = self.wait.until(EC.element_to_be_clickable((By.NAME,txtbirthday_name)))
        birthday_input.send_keys(birthday)

    def SelectAwards(self):
        awards_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, txtawards_xpath)))
        awards_button.click()
        awards_dropdown = self.wait.until(EC.visibility_of_element_located((By.XPATH, buttonawards_xpath)))
        awards_dropdown.click()

    def SelectPageTopic(self, value):
        pagetopic_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, txtpage_xpath)))
        pagetopic_button.click()
        page_value = self.wait.until(EC.element_to_be_clickable((By.NAME, txtpagevalue_name)))
        page_value.click()
        select = Select(page_value)
        select.select_by_visible_text(value)

    def SelectGender(self):
        gender_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, txtgender_xpath)))
        gender_button.click()
        gender_value = self.wait.until(EC.visibility_of_element_located((By.XPATH, buttongender_xpath)))
        gender_value.click()

