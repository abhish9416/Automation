import os
import time

from PageObjects.Homepage import HomePage
from PageObjects.RegistrationPage import RegistrationPage
from Utilities import Random_data
from Utilities.logger import LogGen
from Utilities.readproperties import ReadConfig
from Utilities import Excelutils

class Test_Registration:
    user_excel = os.path.abspath(os.curdir)+'\\TestData\\userdetails.xlsx'
    URL = ReadConfig.getHomepageurl()
    log = LogGen.getlogger()
    next_row = Excelutils.next_empty_row(user_excel,"Sheet1")
    def test_VerifyRegistration(self,setup):
        self.driver = setup
        self.driver.get(self.URL)
        #Operations on Home_Page
        self.log.info("Launching the Browser")
        self.hp = HomePage(self.driver)
        self.hp.clickRegister()
        self.log.info("Clicking on Registration CTA {self.hp.clickRegister()}")

        #Operations of Registration Page
        self.rg = RegistrationPage(self.driver)
        self.rg.clickMaleRadio()
        self.first_name = Random_data.first_name_gen()
        self.last_name = Random_data.last_name_gen()
        self.email = Random_data.email_gen()
        self.rg.setNameAndEmail(self.first_name,self.last_name,self.email)
        self.rg.setDob()
        self.rg.setCompany(ReadConfig.getcompany())
        self.rg.setpassword(ReadConfig.getpassword())
        self.rg.confpassword(ReadConfig.getpassword())
        self.rg.clickregister()
        self.message = self.rg.cnfmessage()

        #validation of Account Creation
        if self.message == "Your registration completed":
            assert True
            Excelutils.write_Data(self.user_excel,"Sheet1",self.next_row,1,self.first_name)
            Excelutils.write_Data(self.user_excel, "Sheet1", self.next_row, 2, self.last_name)
            Excelutils.write_Data(self.user_excel, "Sheet1", self.next_row, 3, self.email)
            Excelutils.write_Data(self.user_excel, "Sheet1", self.next_row, 4, ReadConfig.getpassword())
            Excelutils.write_Data(self.user_excel,"Sheet1",self.next_row,5,"Account Created")
            Excelutils.fill_green_color(self.user_excel,"Sheet1",self.next_row,5)
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\Screenshots\\" + "test_VerifyRegistration.png")
            self.driver.close()
            assert False

