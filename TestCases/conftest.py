import pytest
from appium import webdriver
import warnings


@pytest.fixture()
def init_driver(request):
    desired_cap = {
        "platformName": "Android",
        "appium:platformVersion": "11",
        "appium:deviceName": "emulator-5554",
        "appium:automationName": "uiautomator2",
        "appium:app": "/Users/venkateshr/Desktop/App/Android/BH4_09282022.apk",
        "appPackage": "com.dmdbrands.balancehealth",
        "appActivity": "com.dmdbrands.balancehealth.MainActivity",
        "appium:noReset": "true"
    }

    # set driver instance
    warnings.simplefilter("ignore")
    web_driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
    web_driver.implicitly_wait(10)
    request.cls.driver = web_driver
    yield
    web_driver.quit()

