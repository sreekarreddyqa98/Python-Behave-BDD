from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Utilities import ConfigReader
import logging
import allure
logger = logging.getLogger()

def before_scenario(context,driver):
    browser_name = ConfigReader.read_configuarion("basic-info","broswer")

    if browser_name.__eq__("Chrome"):
        ops = webdriver.ChromeOptions()
        ops.add_argument("--headless=new")
        ops.add_argument("--window-size=1920,1080")
        ops.add_argument("--no-sandbox")
        context.driver = webdriver.Chrome(options=ops)
    elif browser_name.__eq__("Edge"):
        context.driver = webdriver.Edge()
    elif browser_name.__eq__("Firefox"):
        context.driver = webdriver.Firefox()

    context.driver.implicitly_wait(5)

def after_scenario(context,driver):
    context.driver.quit()

def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png()
                      ,name = "failed_screenshot"
                      , attachment_type=AttachmentType.PNG)

