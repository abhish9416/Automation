import os.path
import time

from utilities.readProperties import ReadConfig
from utilities import Excelutils
from pageObjects.HomePage import HomePage
from pageObjects.loginPage import LoginPage
from pageObjects.MyAccount import MyAccount

class Test_Loginddt:
    base_Url = ReadConfig.getApplicationURL()
    path = os.path.abspath(os.curdir) + "\\testdata\\Opencart_LoginData.xlsx"

    def test_loginddt(self,setup):
        row = Excelutils.getrowcount(self.path, "Sheet1")
        lst_status = []
        self.driver = setup
        self.driver.get(self.base_Url)

        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.myact = MyAccount(self.driver)


        for r in range(2, row + 1):
            self.hp.clickMyAccount()
            self.hp.clicklogin()

            self.email = Excelutils.readData(self.path, "Sheet1", r, 1)
            self.password = Excelutils.readData(self.path, "Sheet1", r, 2)
            self.exp = Excelutils.readData(self.path, "Sheet1", r, 3)
            self.lp.setemail(self.email)
            self.lp.setpassword(self.password)
            self.lp.clickloginbtn()
            time.sleep(3)
            self.targetpage = self.lp.account_cnf_message()

            if self.exp == 'Valid':
                if self.targetpage == True:
                    lst_status.append('Pass')
                    self.myact.logoutclick()
                else:
                    lst_status.append('Fail')
            elif self.exp == 'Invalid':
                if self.targetpage == True:
                    lst_status.append('Fail')
                    self.myact.logoutclick()
                else:
                    lst_status.append('Pass')
        self.driver.close()
        # final validation
        if "Fail" not in lst_status:
            assert True
        else:
            assert False

