import inspect
import logging
import os


class LogGen:
    @staticmethod
    def getlogger():
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler(os.path.abspath(os.curdir)+'\\Logs\\automation.log')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger