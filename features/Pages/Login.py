from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Utilities import ConfigReader
import Utilities.BaseUtils as BU


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    USERNAME_TXTBOX = {"by": "xpath", "value": '//input[@name="username"]'}
    PASSWORD_TXTBOX = {"by": "xpath", "value": '//input[@name="password"]'}
    LOGIN_BUTTON = {"by": "xpath", "value": '//button[text()=" Login "]'}

    def enter_username(self, username):
        BU.get_element_by_locator_name(self.driver, self.USERNAME_TXTBOX).send_keys(username)
        # self.driver.find_element(By.XPATH,self.USERNAME_TXTBOX).send_keys(username)

    def clear_username(self):
        BU.get_element_by_locator_name(self.driver, self.USERNAME_TXTBOX).clear()

    def enter_password(self, password):
        BU.get_element_by_locator_name(self.driver, self.PASSWORD_TXTBOX).send_keys(password)

    def clear_password(self):
        BU.get_element_by_locator_name(self.driver, self.PASSWORD_TXTBOX).clear()

    def click_login(self):
        BU.get_element_by_locator_name(self.driver, self.LOGIN_BUTTON).click()
