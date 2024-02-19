from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import pytest

from pom_page import ImdbSearchPage


def test_search(driver):
    search_page=ImdbSearchPage(driver)
    search_page.open_page("https://www.imdb.com/search/name/")
    driver.execute_script("window.scrollTo(0,400);")
    search_page.enter_name("Jayalalitha J")
    search_page.enter_birthdate("24/02/1948","24/02/1948")
    driver.execute_script("window.scrollTo(0,300);")
    search_page.enter_birthday("02-24")
    search_page.select_awards()
    search_page.select_pagetopics()
    driver.execute_script("window.scrollTo(0,300);")
    search_page.enter_deathdate("05/12/2016","05/12/2016")
    search_page.select_gender()
    search_page.seeresult()