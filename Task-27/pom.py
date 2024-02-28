import openpyxl
import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from xl_utilities import *
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def login(self):
        try:
            file_path = "C:\\Users\\91637\\Desktop\\Selenium\\testdata.xlsx"

            # Load the workbook
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active  # Get the active sheet


            sheet.append(["Test ID", "Username", "Password", "Date", "Time", "Tester", "Test Result"])

            rows = getRowCount(file_path, "Sheet")
            for r in range(2, rows + 1):
                username = readData(file_path, "Sheet", r, 2)
                password = readData(file_path, "Sheet", r, 3)

                self.wait.until(EC.presence_of_element_located((By.NAME, "username"))).clear()
                self.wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(username)

                self.wait.until(EC.presence_of_element_located((By.NAME, "password"))).clear()
                self.wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys(password)

                login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button")))
                login_button.click()

                # Check if the current URL contains "dashboard"
                if "dashboard" in self.driver.current_url.lower():
                    print("Test Passed")
                    sheet.append([r - 1, username, password, time.strftime("%Y-%m-%d"), time.strftime("%H:%M:%S"), "priya", "Pass"])
                    fillGreenColor(file_path, "Sheet", r, 7)
                else:
                    print("Test Failed")
                    sheet.append([r - 1, username, password, time.strftime("%Y-%m-%d"), time.strftime("%H:%M:%S"), "priya", "Fail"])
                    fillRedColor(file_path, "Sheet", r, 7)

            workbook.save(file_path)

        except Exception as e:
            print(f"Error occurred: {e}")
