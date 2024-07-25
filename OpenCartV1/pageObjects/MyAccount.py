from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.HomePage import HomePage
class MyAccount():
    btn_Logout_XPATH = "//ul[@class='dropdown-menu dropdown-menu-right']//li[5]//a"
    btn_myaacount_xpath = "//span[contains(text(),'My Account')]"
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(driver, 10, ignored_exceptions=[Exception])

    def logoutclick(self):
        self.driver.find_element(By.XPATH,self.btn_myaacount_xpath).click()
        self.driver.find_element(By.XPATH,self.btn_Logout_XPATH).click()