from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Utilities import ConfigReader
from features.Pages.Login import LoginPage
from features.Pages.Dashboard_Page import DashboardPage



@given(u'I navigate to "{url}"')
def step_impl(context,url):
    context.Login_Page = LoginPage(context.driver)
    context.driver.get(ConfigReader.read_configuarion("basic-info",url))
    # time.sleep(5)
    print(context.driver.title)

@when(u'I enter "{username}" in the "USERNAME_TXTBOX" field')
def step_impl(context,username):
    context.Login_Page.clear_username()
    context.Login_Page.enter_username(username)


@when(u'I enter "{password}" in the "PASSWORD_TEXTBOX" field')
def step_impl(context,password):
    context.Login_Page.clear_password()
    context.Login_Page.enter_password(password)


@when(u'I click on the "LOGIN" button')
def step_impl(context):
    context.Login_Page.click_login()


@then(u'I should be in "DASBOARD" page')
def step_impl(context):
    context.Dashboard_page = DashboardPage(context.driver)
    print("result : " + str(context.Dashboard_page.dahshboard_page_is_displayed()))
    assert context.Dashboard_page.dahshboard_page_is_displayed() == True
    # time.sleep(5)
