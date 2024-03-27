#import selenium webdriver
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
#import expected conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import pyautogui
import time

# login page locators
username_txt= "username"
password_txt = "password"
login_butn= ".oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button"

#pim module locators
pim_module="//span[normalize-space()='PIM']"
add_butn="//button[normalize-space()='Add']"
first_name="firstName"
last_name="lastName"
middle_name="middleName"
image_ele="//img[@class='employee-image']"
file_path="C:\\Users\91637\Desktop\Selenium\pic.jpg"
save_butn="//button[normalize-space()='Save']"

#other details field locators
other_id="//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-3 orangehrm-full-width-grid']/div[2]/div[1]/div[2]/input[1]"
driver_linum="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input"
li_expiray_date="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input"
nationality_ele="//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//div[@class='oxd-grid-3 orangehrm-full-width-grid']//div[1]//div[1]//div[2]//div[1]//div[1]//div[1]"
marital_status="//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//div[2]//div[1]//div[2]//div[1]//div[1]//div[1]"
date_birth="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input"
gender_ele="//label[normalize-space()='Female']"
save_butn1="//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit'][normalize-space()='Save']"

#custom fields
blood_type="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]"
blood_dropdown="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]"
test_field="//div[@class='orangehrm-custom-fields']//div[@class='orangehrm-card-container'"
save_butn2="//div[@class='orangehrm-custom-fields']//button[@type='submit'][normalize-space()='Save']"

#attachment locators
add_attachment_butn="//button[normalize-space()='Add']"
browse_butn="//div[@class='oxd-file-input-div']"
comment_ele="//textarea[@placeholder='Type comment here']"
save_butn3="//div[@class='orangehrm-attachment']//button[@type='submit'][normalize-space()='Save']"

#edit employee page locators
hoverempxpath="//a[normalize-space()='Employee List']"
selempxpath="//div[contains(text(),'priya')]"
edit_firstnamepath="//input[@placeholder='First Name']"
edit_lastnamepath="//input[@placeholder='Last Name']"
edit_otherid_path="//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-3 orangehrm-full-width-grid']/div[2]/div[1]/div[2]/input[1]"
edit_driverlicense="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input"
edit_liexpdate_path="//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-3 orangehrm-full-width-grid']/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]"
edit_martialclass="//label[normalize-space()='Male']"
buttonsavexpath="//button[@type='submit']"
delempclass="//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[5]/div/div[9]/div/button[1]"
buttondeletexpath="//button[normalize-space()='Yes, Delete']"

class OrangeHRM:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

#create a function for valid login
    def valid_login(self, username, password):
        self.wait.until(EC.visibility_of_element_located((By.NAME,username_txt))).send_keys(username)
        self.wait.until(EC.visibility_of_element_located((By.NAME,password_txt))).send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,login_butn))).click()

#create function for invali login
    def invalid_login(self, in_username, in_password):
        self.wait.until(EC.visibility_of_element_located((By.NAME,username_txt))).send_keys(in_username)
        self.wait.until(EC.visibility_of_element_located((By.NAME,password_txt))).send_keys(in_password)   #click login buttun
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,login_butn))).click()

#create function for  add employee
    def add_employee(self, firstname, middlename, lastname,oth_id,lie_num,lie_exdate,birth_day,test_txt,comment_txt):
        #click pim module
        self.wait.until(EC.element_to_be_clickable((By.XPATH,pim_module))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,add_butn))).click()                 #click add employee
        self.wait.until(EC.visibility_of_element_located((By.NAME,first_name ))).send_keys(firstname)   #enter first name
        self.wait.until(EC.visibility_of_element_located((By.NAME,middle_name))).send_keys(middlename)   #enter middle name
        self.wait.until(EC.visibility_of_element_located((By.NAME,last_name))).send_keys(lastname)       
        #upload image
        self.wait.until(EC.element_to_be_clickable((By.XPATH,image_ele))).click()
        pyautogui.write(file_path)
        time.sleep(5)
        pyautogui.press('enter')
        self.wait.until(EC.element_to_be_clickable((By.XPATH,save_butn))).click()

        # enter personal details
        self.wait.until(EC.presence_of_element_located((By.XPATH,other_id))).send_keys(oth_id) # enter other id
        self.wait.until(EC.presence_of_element_located((By.XPATH,driver_linum))).send_keys(lie_num)  # enter driver lisence number
        self.wait.until(EC.visibility_of_element_located((By.XPATH,li_expiray_date ))).send_keys(lie_exdate)  # enter the lisence expiray date
        # select nationality
        # sel_marital_status = self.wait.until(EC.element_to_be_clickable((By.XPATH,nationality_ele ))).click()
        # sel_marital_status.select_by_visisble_text("Indian")
        # enter maruital status
        # sel_marital_status = self.wait.until(EC.element_to_be_clickable((By.XPATH,marital_status ))).click()
        # sel_marital_status.select_by_visisble_text("signle")
        self.wait.until(EC.presence_of_element_located((By.XPATH, date_birth))).send_keys(birth_day)   # enter date of birth
        self.wait.until(EC.element_to_be_clickable((By.XPATH, gender_ele))).click()     # select gender
        self.wait.until(EC.element_to_be_clickable((By.XPATH,save_butn1))).click()       # click save button    
 # custom fields  
        # select blood type
        self.wait.until(EC.element_to_be_clickable((By.XPATH,blood_type))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,blood_dropdown))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, date_birth))).send_keys(test_txt)    # enter test field
        self.wait.until(EC.element_to_be_clickable((By.XPATH,save_butn2))).click()     # click save button
        # attachment field
        self.wait.until(EC.element_to_be_clickable((By.XPATH,add_attachment_butn))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,browse_butn))).click()
        # enter the image file
        pyautogui.write(file_path)
        pyautogui.press('enter')
        self.wait.until(EC.presence_of_element_located((By.XPATH,comment_ele))).send_keys(comment_txt) # enter comment
        self.wait.until(EC.element_to_be_clickable((By.XPATH,save_butn3))).click()

#create function for edit the employee
    def edit_employee(self,new_fname,new_lname,new_linum,new_otherid,new_liexp_date):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, pim_module))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,selempxpath))).click()   #select the employee for edit
        #edit first name
        update_fname=self.wait.until(EC.visibility_of_element_located((By.XPATH,edit_firstnamepath)))
        update_fname.clear()
        update_fname.send_keys(new_fname)
        update_lname=self.wait.until(EC.visibility_of_element_located((By.XPATH, edit_lastnamepath)))  #edit last name
        update_lname.clear()
        update_fname.send_keys(new_lname)
        update_otherid = self.wait.until(EC.visibility_of_element_located((By.XPATH, edit_otherid_path)))  #edit other id
        update_otherid.clear()
        update_otherid.send_keys(new_otherid)
        update_linumber = self.wait.until(EC.visibility_of_element_located((By.XPATH,edit_driverlicense)))   #edit diver lisence
        update_linumber.clear()
        update_linumber.send_keys(new_linum)
        update_liexp_date = self.wait.until(EC.visibility_of_element_located((By.XPATH, edit_liexpdate_path)))   # edit diver lisence expiry date
        update_liexp_date.clear()
        update_liexp_date.send_keys(new_liexp_date)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, edit_martialclass))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, buttonsavexpath))).click()

        # veify first name value
        updated_first_name = update_fname.get_attribute("value")
        print("Updated last name:", updated_first_name)

        # Verify last name field value
        updated_last_name = update_lname.get_attribute("value")
        print("Updated last name:", updated_last_name)

        # #verify the other id field
        updated_otherid = update_otherid.get_attribute("value")
        print("Updated otherid:", updated_otherid)

       #verify the lisence number
        updated_lisence_num = update_linumber.get_attribute("value")
        print("Updated lisence number:", updated_lisence_num)

      #verify the lisence expiray date
        updated_liexp_date = update_liexp_date.get_attribute("value")
        print("Updated lisence exp date:", updated_liexp_date)

#create a function for delete the employee in the list
    def del_employee(self):
        #click pim module
        self.wait.until(EC.element_to_be_clickable((By.XPATH, pim_module))).click()
        # select the employee
        self.wait.until(EC.element_to_be_clickable((By.XPATH, hoverempxpath))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, delempclass))).click()
        #delete the employee
        self.wait.until(EC.element_to_be_clickable((By.XPATH, buttondeletexpath))).click()
