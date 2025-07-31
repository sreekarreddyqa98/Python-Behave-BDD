from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Utilities import ConfigReader
import Utilities.BaseUtils as BU

class DashboardPage:

    def __init__(self,driver):
        self.driver = driver


    DASHBOARD_PAGE_TITLE = {"by": "xpath", "value": '//h6[text()="Dashboard"]'}


    def dahshboard_page_is_displayed(self):
        self.result = BU.get_element_by_locator_name(self.driver, self.DASHBOARD_PAGE_TITLE).text == "Dashboard"
        return  self.result