from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

class LoginPage():
    txt_email_XPATH = "//input[@name='email']"
    txt_password_XPATH = "//input[@name='password']"
    btn_login_XPATH = "//input[@value='Login']"
    msg_myaccount_XPATH = "//h2[normalize-space()='My Account']"
    msg_invalidcrde_XPATH = "//div[@class='alert alert-danger alert-dismissible']"

    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(driver,10,ignored_exceptions=[Exception])

    def setemail(self,email):
        self.email_input = self.driver.find_element(By.XPATH,self.txt_email_XPATH)
        self.email_input.clear()
        self.email_input.send_keys(email)

    def setpassword(self,password):
        self.password_input = self.driver.find_element(By.XPATH, self.txt_password_XPATH)
        self.password_input.clear()
        self.password_input.send_keys(password)
    def clickloginbtn (self):
        self.driver.find_element(By.XPATH,self.btn_login_XPATH).click()

    def account_cnf_message(self):
        try:
            return self.driver.find_element(By.XPATH,self.msg_myaccount_XPATH).is_displayed()
        except Exception:
            None

    def login_error_message(self):
        try:
            return self.driver.find_element(By.XPATH,self.msg_invalidcrde_XPATH).is_displayed()
        except Exception:
            None
