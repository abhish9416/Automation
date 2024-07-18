import datetime
import os.path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from datetime import datetime


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        chrome_ops = webdriver.ChromeOptions()
        chrome_ops.add_argument("--disable-notifications")
        chrome_ops.add_argument("--disable-extensions")
        chrome_ops.add_argument("--disable-infobars")
        chrome_ops.add_argument("--start-maximized")
        chrome_ops.add_argument("--disable-blink-features=AutomationControlled")
        # chrome_ops.add_argument("--headless")
        chrome_ops.add_argument("--disable-gpu")
        chrome_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service =chrome_service,options=chrome_ops)
        print("Chrome Browser Started Successfully")

    elif browser == "firefox":
        firefox_ops = webdriver.FirefoxOptions()
        firefox_ops.add_argument("--disable-notifications")
        firefox_ops.add_argument("--disable-extensions")
        firefox_ops.add_argument("--disable-infobars")
        firefox_ops.add_argument("--start-maximized")
        # firefox_ops.add_argument("--headless")
        firefox_ops.add_argument("--disable-gpu")
        firefox_service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=firefox_service,options=firefox_ops)
        print("Firefox Browser Started Successfully")
    elif browser == "edge":
        edge_ops = webdriver.EdgeOptions()
        edge_ops.add_argument("--disable-notifications")
        edge_ops.add_argument("--disable-extensions")
        edge_ops.add_argument("--disable-infobars")
        edge_ops.add_argument("--start-maximized")
        # edge_ops.add_argument("--headless")
        edge_ops.add_argument("--disable-gpu")
        edge_service = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Firefox(service=edge_service,options=edge_ops)
        print("Edge Browser Started Successfully")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser",default = "chrome")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#################--Pytest HTML Report--####################
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Abhishek'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"