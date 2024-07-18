import time
import os
import pytest
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.HomePage import HomePage
from utilities import fakedatagenerator
from utilities.readProperties import ReadConfig
from utilities import Excelutils


class Test_AccountRegistration:
    base_url = ReadConfig.getApplicationURL()
    Excel_file = os.path.abspath(os.curdir)+"\\testData\\Userdetail.xlsx"
    rows = Excelutils.getrowcount(Excel_file, "Sheet1")

    @pytest.mark.sanity
    def test_accountreg(self, setup):
        # Driver Operation
        self.driver = setup
        self.driver.get(self.base_url)

        # Cicking on registration link through homepage
        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        # operations on registeration page
        self.register = AccountRegistrationPage(self.driver)
        self.first_name = fakedatagenerator.firstnamegenerator()
        self.register.setfirstname(self.first_name)
        self.last_name = fakedatagenerator.lastnamegenerator()
        self.register.setlastname(self.last_name)
        self.email_add = fakedatagenerator.emailgenerator()
        self.register.setemail(self.email_add)
        self.phone_number = fakedatagenerator.phonegeneratore()
        self.register.setphone(self.phone_number)
        self.password = ReadConfig.getPassword()
        self.register.setpassword(self.password)
        self.register.setcnfpassword(ReadConfig.getPassword())
        self.register.clickradioyes()
        self.register.clickcheckbox()
        self.register.clickcontinue()
        self.msg = self.register.cnfmessage()
        if self.msg == "Your Account Has Been Created!":
                next_row = Excelutils.get_next_empty_row(self.Excel_file,"Sheet1")
                Excelutils.writedata(self.Excel_file, "Sheet1", next_row, 1,self.first_name)
                Excelutils.writedata(self.Excel_file,"Sheet1",next_row,2,self.last_name)
                Excelutils.writedata(self.Excel_file, "Sheet1", next_row, 3, self.email_add)
                Excelutils.writedata(self.Excel_file, "Sheet1", next_row, 4, self.phone_number)
                Excelutils.writedata(self.Excel_file, "Sheet1", next_row, 5, self.password)
                Excelutils.writedata(self.Excel_file, "Sheet1", next_row, 6,"Account Created")
                Excelutils.fillgreencolour(self.Excel_file,"Sheet1",next_row,6)
                assert True
                self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_accountreg.png")

            self.driver.close()
            assert False
        time.sleep(5)
