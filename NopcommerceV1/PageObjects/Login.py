from selenium.webdriver.common.by import By


class Login:
    input_email_XPATH = "//input[@name='Email']"
    input_password_XPATH = "//input[@name='Password']"
    btn_Login_XPATH = "//button[contains(text(),'Log in')]"
    def __init__(self,driver):
        self.driver = driver

    def set_email(self,email):
        self.driver.find_element(By.XPATH,self.input_email_XPATH).send_keys(email)
    def set_password(self,pwd):
        self.driver.find_element(By.XPATH,self.input_password_XPATH).send_keys(pwd)
    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.btn_Login_XPATH).click()