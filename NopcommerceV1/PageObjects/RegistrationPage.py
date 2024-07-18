from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select


class RegistrationPage:
    radio_Male_XPATH = "//input[@value='M']"
    radio_Female_XPATH = "//input[@value='F']"
    input_FirstName_XPATH = "//input[@name='FirstName']"
    input_Last_Name_Xpath = "//input[@name='LastName']"
    input_Email_Xpath = "//input[@name='Email']"
    dropdown_Day_XPATH = "//select[@name='DateOfBirthDay']"
    dropdown_month_XPATH = "//select[@name='DateOfBirthMonth']"
    dropdown_year_XPATH = "//select[@name='DateOfBirthYear']"
    input_Company_XPATH = "//input[@name='Company']"
    input_password_XPATH = "//input[@name='Password']"
    input_Confirmpwd_XPATH = "//input[@name='ConfirmPassword']"
    msg_confirm_XPATH = "//div[@class='result']"
    btn_register_XPATH = "//button[@name='register-button']"
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def clickMaleRadio(self):
        self.driver.find_element(By.XPATH,self.radio_Male_XPATH).click()

    def clickFemaleRadio(self):
        self.driver.find_element(By.XPATH,self.radio_Female_XPATH).click()

    def setNameAndEmail(self,fname,lname,email):
        self.driver.find_element(By.XPATH,self.input_FirstName_XPATH).send_keys(fname)
        self.driver.find_element(By.XPATH,self.input_Last_Name_Xpath).send_keys(lname)
        self.driver.find_element(By.XPATH,self.input_Email_Xpath).send_keys(email)

    def setDob(self):
        self.day = Select(self.driver.find_element(By.XPATH,self.dropdown_Day_XPATH))
        self.day.select_by_value("16")
        self.month = Select(self.driver.find_element(By.XPATH,self.dropdown_month_XPATH))
        self.month.select_by_value("8")
        self.year = Select(self.driver.find_element(By.XPATH,self.dropdown_year_XPATH))
        self.year.select_by_value("1998")

    def setCompany(self,company):
        self.driver.find_element(By.XPATH,self.input_Company_XPATH).send_keys(company)

    def setpassword(self,pwd):
        self.driver.find_element(By.XPATH,self.input_password_XPATH).send_keys(pwd)

    def confpassword(self,cnfpwd):
        self.driver.find_element(By.XPATH,self.input_Confirmpwd_XPATH).send_keys(cnfpwd)

    def clickregister(self):
        self.driver.find_element(By.XPATH,self.btn_register_XPATH).click()

    def cnfmessage(self):
        return self.driver.find_element(By.XPATH,self.msg_confirm_XPATH).text