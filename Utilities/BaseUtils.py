from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Utilities import ConfigReader
import logging
logger = logging.getLogger()

def get_locator(type):
    try:
        type = type.upper()
        if type == "ID":
            locator_by = By.ID
        elif type == "XPATH":
            locator_by = By.XPATH
        elif type == "LINK_TEXT":
            locator_by = By.LINK_TEXT
        elif type == "PARTIAL_LINK_TEXT":
            locator_by = By.PARTIAL_LINK_TEXT
        elif type == "NAME":
            locator_by = By.NAME
        elif type == "TAG_NAME":
            locator_by = By.TAG_NAME
        elif type == "CLASS_NAME":
            locator_by = By.CLASS_NAME
        elif type == "CSS_SELECTOR":
            locator_by = By.CSS_SELECTOR
        else:
            raise ValueError("Unknown locator by type: " + type)
        return locator_by
    except Exception as err:
        logger.error(str(err))
        raise ValueError(str(err))

def get_element_by_locator_name(driver, locator):
    return driver.find_element(get_locator(locator.get("by")),locator.get("value"))


def get_elements_by_locator_name(driver,type, name):
    return driver.find_elements(get_locator(type),name)
