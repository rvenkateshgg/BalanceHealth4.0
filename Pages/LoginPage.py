from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    Login_link = (AppiumBy.XPATH, "//android.view.View[@content-desc='LOG IN']")
    SignUP_link = (AppiumBy.XPATH,"//android.view.View[@content-desc='SIGN UP']")
    USERNAME = (AppiumBy.XPATH, "//android.widget.EditText[@index='0']")
    PASSWORD = (AppiumBy.XPATH, "(//android.widget.EditText[@index='0'])[2]")
    Login_btn = (AppiumBy.XPATH, "//android.widget.Button[@text='LOG IN']")
    MONTH_Btn = (AppiumBy.XPATH,"//android.widget.Button[@text='MONTH']")

    def __int__(self, driver):
        super().__init__(driver)

    def click_Signup_link(self):
        self.do_click(self.SignUP_link)

    def back(self):
        return self.do_Backward()

    def click_login_link(self):
        self.do_click(self.Login_link)

    def get_Login_text(self):
        return self.get_element_text(self.Login_btn)

    def do_login(self, username, password):
        self.do_sendkeys(self.USERNAME, username)
        self.do_sendkeys(self.PASSWORD, password)
        self.do_click(self.Login_btn)

    def try_findElement(self):
        self.do_findOut_element(self.MONTH_Btn)

