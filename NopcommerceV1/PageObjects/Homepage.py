from selenium.webdriver.common.by import By


class HomePage:
    btn_Register_XPATH = "//a[text()='Register']"
    btn_Login_XPATH = "//a[text()='Log in']"
    btn_Wishlist_XPATH = "//span[text()='Wishlist']"
    btn_ShoppingCart_XPATH = "//span[text()='Shopping cart']"
    def __init__(self,driver):
        self.driver = driver

    def clickRegister(self):
        self.driver.find_element(By.XPATH,self.btn_Register_XPATH).click()

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_Login_XPATH).click()

    def clickWishlist(self):
        self.driver.find_element(By.XPATH,self.btn_Wishlist_XPATH).click()

    def clickCart(self):
        self.driver.find_element(By.XPATH,self.btn_ShoppingCart_XPATH).click()