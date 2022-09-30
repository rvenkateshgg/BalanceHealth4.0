from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from Pages.BasePage import BasePage


class HomePage(BasePage):

    Menu_Btn = "//android.widget.Button[@text='Menu']"
    Account_Link = "//android.view.View[@text='ACCOUNT']"
    LogOut_Btn = "//android.view.View[@text='LOGOUT']"
    Log_Out = "//android.widget.Button[@text='LOG OUT']"
    LOgIn_lnk = "//android.view.View[@content-desc='LOG IN']"

    def __int__(self, driver):
        super().__init__(driver)

    def Click_Menu(self):
        self.do_click(self.Menu_Btn)

    def Click_Account_lnk(self):
        self.do_click(self.Account_Link)

    def Click_LogOut_lnk(self):
        self.do_click(self.LogOut_Btn)

    def do_Logout(self):
        self.do_click(self.Log_Out)

    def FinOut_Login_lnk(self):
        self.do_findOut_element(self.LOgIn_lnk)
