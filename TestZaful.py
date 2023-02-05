import unittest

from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestZaful(unittest.TestCase):

    valid_email = "asdsadszazdzzz@o2.pl"
    valid_password = "1234567g"

    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.zaful",
            "appActivity": "com.zaful.framework.module.system.activity.MainActivity"
        }

        # Start the Appium client
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()

    def testValidateUserSeeDiscountTextAfterRegister(self):
        account_btn = self.driver.find_element(AppiumBy.ID, "com.zaful:id/nav_account")
        account_btn.click()

        login_btn = self.driver.find_element(AppiumBy.ID, "com.zaful:id/llLoginGuide")
        login_btn.click()

        email_field = self.driver.find_element(AppiumBy.ID, "com.zaful:id/etRegisterEmail")
        email_field.send_keys(self.valid_email)

        password_field = self.driver.find_element(AppiumBy.ID, "com.zaful:id/etRegisterPassword")
        password_field.send_keys(self.valid_password)

        policy_check = self.driver.find_element(AppiumBy.ID, "com.zaful:id/cbPrivacyPolicy")
        policy_check.click()

        register_btn = self.driver.find_element(AppiumBy.ID, "com.zaful:id/btRegister")
        register_btn.click()

        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='Discount for new user only']")))

        discount_text = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Discount for new user only']").is_displayed()

        self.assertEqual(discount_text, True)


if __name__ == '__main__':
    unittest.main()
