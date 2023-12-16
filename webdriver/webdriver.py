from appium import webdriver
from appium.options.android import UiAutomator2Options


class Driver:
    def __init__(self):
        caps = {
            "platformName": "Android",
            "appium:automationName": "UiAutomator2",
            "appium:appPackage": "com.android.calculator2",
            "appium:appActivity": ".Calculator",
            "appium:ensureWebviewsHavePages": True,
            "appium:nativeWebScreenshot": True,
            "appium:newCommandTimeout": 3600,
            "appium:connectHardwareKeyboard": True
        }
        options = UiAutomator2Options()
        options.load_capabilities(caps=caps)
        self.instance = webdriver.Remote("http://127.0.0.1:4723", options=options)
