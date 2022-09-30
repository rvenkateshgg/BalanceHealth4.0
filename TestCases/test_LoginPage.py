import time

import pytest
from appium import webdriver

from Pages.BasePage import BasePage
from TestCases.test_Base import BaseTest
from Pages.LoginPage import LoginPage
from Config.config import TestData


class Test_Login(BaseTest):

    def test_LoginPage(self):
        self.loginPage = LoginPage(self.driver)
        #self.loginPage.click_Signup_link()
        self.loginPage.back()
        self.loginPage.click_login_link()
        print(self.loginPage.get_Login_text())
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        try:
            self.loginPage.try_findElement()
            print("HomePage reached successfully")
        except:
            print("Error or Fail")
        time.sleep(3)
