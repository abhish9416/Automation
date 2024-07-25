import time

import pytest

from utilities.readProperties import ReadConfig
from pageObjects.loginPage import LoginPage
from pageObjects.HomePage import HomePage
from pageObjects.MyAccount import MyAccount
from utilities import Excelutils
import os

class Test_login:
    base_url = ReadConfig.getApplicationURL()
    Excel_file = os.path.abspath(os.curdir) + "\\testData\\Userdetail.xlsx"
    def test_login(self,setup,email,password):
        self.driver = setup
        self.driver.get(self.base_url)

        self.homepage = HomePage(self.driver)
        self.myact = MyAccount(self.driver)
        self.homepage.clickMyAccount()
        self.homepage.clicklogin()
        self.login = LoginPage(self.driver)
        self.login.setemail(email)
        self.login.setpassword(password)
        self.login.clickloginbtn()
        self.message = self.login.account_cnf_message()
        self.errmessage = self.login.login_error_message()

    @pytest.mark.sanity
    def test_validLogin(self,setup):
        self.email = Excelutils.readData(self.Excel_file,"Sheet1",2,3)
        self.password = Excelutils.readData(self.Excel_file,"Sheet1",2,5)
        self.test_login(setup,self.email,self.password)
        # Test Case Validation for Valid input using account confirmation message
        if self.message:
            print("Test Case Passed and Login is successful")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\" + "test_login.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_InvalidLogin(self,setup):
        self.email = "abhishek123@gmail.com"
        self.password = "Admin123"
        self.test_login(setup,self.email,self.password)
        if self.errmessage:
            print("Test Case Passed")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login.png")
            self.driver.close()
            assert False








