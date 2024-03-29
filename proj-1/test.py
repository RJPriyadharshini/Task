from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# import the page objects from pom file
from pom import OrangeHRM

error_text = "//div[@role='alert']"


try:
         # testcase_01 valid login
    def test1_valid_login(browser):
        login_page = OrangeHRM(browser)
        login_page.valid_login("Admin", "admin123")
        if "dashboard" in browser.current_url:
            print("login successful")
        else:
            print("login not successful")


        # testcase_02 invalid login
    def test2_invalid_login(browser):
        login_page = OrangeHRM(browser)
        login_page.invalid_login("priya", "admin1")
        error_message = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, error_text)))
        print("invalid login error message:", error_message.text)
        assert error_message.text == "Invalid credentials", "Error message is not displayed correctly

        # testcase_3 add new employee
    def test3_add_employee(browser):

        login_page = OrangeHRM(browser)
        login_page.valid_login("Admin", "admin123")
        add_user = OrangeHRM(browser)
        add_user.add_employee("priya", "data", "G", "123", "3434", "2024-04-11", "2000-07-07", "add employee",
                              "employee added")
        print("Employee added successfully")

        # testcase_4 edit the existing employee
    def test4_edit_employee(browser):
        login_page = OrangeHRM(browser)
        login_page.valid_login("Admin", "admin123")
        add_user = OrangeHRM(browser)
        add_user.edit_employee("dharshan", "G", "4343", "98", "2022-09-09")
        print("Employee updated successfully")

        # testcase_5 delete the employee
    def test5_del_employee(browser):

        login_page = OrangeHRM(browser)
        login_page.valid_login("Admin", "admin123")
        del_user = OrangeHRM(browser)
        del_user.del_employee()
        print("employee deleted successfully")
except Exception as e:
    print("error message as ", e)
