import inspect
import logging
from logging import getLogger
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures('driver')
class BaseClass:

    @staticmethod
    def getLogger():
        loggerName = inspect.stack()[1][3]
        logger = getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter('%(asctime)s :%(levelname)s : %(name)s : %(message)s')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def verifyCSSPresence(driver, cssLocator):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, cssLocator)))

    @staticmethod
    def verifyUrlPresence(driver, url):
        WebDriverWait(driver, 10).until(EC.url_to_be(url))

    @staticmethod
    def verifyVisibilityOfElement(driver, locator):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))





