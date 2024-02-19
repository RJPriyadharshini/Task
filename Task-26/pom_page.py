import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ImdbSearchPage:

    def __init__(self,driver):
        self.driver= driver

        self.name_element=(By.XPATH,"//div[contains(text(),'Name')]")
        self.name_input=(By.NAME, "name-text-input")
        self.birthdate_element=(By.XPATH,"//*[@id='birthDateAccordion']")
        self.birth_start_input =(By.NAME, "birth-date-start-input")
        self.birth_end_input =(By.NAME, "birth-date-end-input")
        self.birthday_element=(By.XPATH, "//div[contains(text(),'Birthday')]")
        self.birthday_input = (By.XPATH, "//input[@id='text-input__13']")
        self.awards_dropdown=(By.XPATH, "//div[contains(text(),'Awards & recognition')]")
        self.awards_button =(By.XPATH, "//button[@class='sc-5fbe012a-0 iOZIrv ipc-chip ipc-chip--filled ipc-chip--on-base-accent1']")
        self.pagetopics_element=(By.XPATH, "//div[contains(text(),'Page topics')]")
        self.page_topics_dropdown =(By.XPATH, "//div[@id='pageTopicsAccordion']//button[4]")
        self.deathdate_element=(By.XPATH, "//div[contains(text(),'Death date')]")
        self.death_date_from_input =(By.XPATH, "//input[@id='text-input__2386']")
        self.death_date_to_input =(By.XPATH, "//input[@id='text-input__2387']")
        self.gender_element=(By.XPATH, "//div[contains(text(),'Gender identity')]")
        self.gender_identity_value =(By.XPATH, "//div[@id='genderIdentityAccordion']//button[2]")
        self.see_results=(By.XPATH,"//span[normalize-space()='See results']")


    def open_page(self,url):
        self.driver.get(url)

    def enter_name(self,name):
        self.driver.find_element(*self.name_element).click()
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.name_element).click()

    def enter_birthdate(self, birthstart,birthend):
        self.driver.find_element(*self.birthdate_element).click()
        self.driver.find_element(*self.birth_start_input).send_keys(birthstart)
        self.driver.find_element(*self.birth_end_input).send_keys(birthend)
        self.driver.find_element(*self.birthdate_element).click()


    def enter_birthday(self,birthday):
        self.driver.find_element(*self.birthday_element).click()
        self.driver.find_element(*self.birthday_input).send_keys(birthday)
        self.driver.find_element(*self.birthday_element).click()

    def select_awards(self):
        self.driver.find_element(*self.awards_dropdown).click()
        self.driver.find_element(*self.awards_button).click()
        self.driver.find_element(*self.awards_dropdown).click()

    def select_pagetopics(self):
        self.driver.find_element(*self.pagetopics_element).click()
        self.driver.find_element(*self.page_topics_dropdown).click()
        self.driver.find_element(*self.pagetopics_element).click()

    def enter_deathdate(self, deathfrom, deathto):
        self.driver.find_element(*self.deathdate_element).click()
        self.driver.find_element(*self.death_date_from_input).send_keys(deathfrom)
        self.driver.find_element(*self.death_date_to_input).send_keys(deathto)
        self.driver.find_element(*self.birthdate_element).click()

    def select_gender(self):
        self.driver.gender_element(*self.gender_element).click()
        self.driver.find_element(*self.gender_identity_value).click()
        self.driver.find_element(*self.gender_element).click()

    def seeresult(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.see_results)
        ).click()
