from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage():
    lnk_my_account_xpath = "//span[contains(text(),'My Account')]"
    lnk_Register_XPATH = "//a[text()='Register']"
    lnk_login_XPATH = "//a[text()='Login']"

    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(driver,10,ignored_exceptions=[Exception])

    def clickMyAccount(self):
        self.account = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.lnk_my_account_xpath)))
        self.account.click()

    def clickRegister(self):
        self.register = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.lnk_Register_XPATH)))
        self.register.click()

    def clicklogin(self):
        self.login = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.lnk_login_XPATH)))
        self.login.click()
