import os.path
import time

from PageObjects.Login import Login
from PageObjects.Homepage import HomePage
from Utilities.readproperties import ReadConfig
from Utilities import Excelutils

class TestLogin:
    def test_Verify_login(self,setup):
        user_file = os.path.abspath(os.curdir)+'\\TestData\\userdetails.xlsx'
        self.driver = setup
        self.driver.get(ReadConfig.getHomepageurl())

        self.hp = HomePage(self.driver)
        self.login = Login(self.driver)

        self.hp.clickLogin()
        # loginpage = self.driver.current_url()
        # if loginpage ==
        self.email = Excelutils.read_Data(user_file,"Sheet1",2,3)
        self.login.set_email(self.email)
        self.password = Excelutils.read_Data(user_file,"Sheet1",2,4)
        self.login.set_password(self.password)
        self.login.clicklogin()
        time.sleep(5)
