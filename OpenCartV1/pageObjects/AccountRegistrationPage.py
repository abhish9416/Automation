from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class AccountRegistrationPage():
    txt_FirstName_XPATH = "//input[@name='firstname']"
    txt_LastName_XPATH = "//input[@name='lastname']"
    txt_Email_XPATH = "//input[@name='email']"
    txt_phone_XPATH = "//input[@name='telephone']"
    txt_Password_XPATH = "//input[@name='password']"
    txt_cnfPassword_XPATH = "//input[@name='confirm']"
    radiobtn_Yes_XPATH = "//label[text()='Yes']"
    radiobtn_No_XPATH = "//input[@id='input-newsletter-no']"
    checkbox_PrivacyPolicy_XPATH = "//input[@name='agree']"
    btn_continue_XPATH = "//input[@value='Continue']"
    msg_confmessage_XPATH = "//div[@id='content']//h1"

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(driver,20,ignored_exceptions=[Exception])

    def setfirstname(self,first_name):
        self.driver.find_element(By.XPATH,self.txt_FirstName_XPATH).send_keys(first_name)

    def setlastname(self,lname):
        self.driver.find_element(By.XPATH,self.txt_LastName_XPATH).send_keys(lname)

    def setemail(self,email):
        self.driver.find_element(By.XPATH,self.txt_Email_XPATH).send_keys(email)
    def setphone(self,pnum):
        self.driver.find_element(By.XPATH,self.txt_phone_XPATH).send_keys(pnum)

    def setpassword(self,pwd):
        self.driver.find_element(By.XPATH,self.txt_Password_XPATH).send_keys(pwd)

    def setcnfpassword(self,cnfpwd):
        self.driver.find_element(By.XPATH,self.txt_cnfPassword_XPATH).send_keys(cnfpwd)

    def clickradioyes(self):
        radio_yes = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.radiobtn_Yes_XPATH)))
        radio_yes.click()

    def clickcheckbox(self):
        checkbox = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.checkbox_PrivacyPolicy_XPATH)))
        checkbox.click()

    def clickcontinue(self):
        btn_continue = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.btn_continue_XPATH)))
        btn_continue.click()

    def cnfmessage(self):

        cnf_message = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.msg_confmessage_XPATH)))
        return cnf_message.text

    def errormessage(self):
        self.driver.find_element





