import configparser
import os.path

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getHomepageurl():
        return config.get('commonInfo','HomePage_URL')

    @staticmethod
    def getpassword():
        return config.get('commonInfo','password')

    @staticmethod
    def getcompany():
        return config.get('commonInfo', 'Company')