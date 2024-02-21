import time
import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from fixtures.base_fixture import OxmaintFixture
from tests import BASE_URL
from fixtures.login import LogIn
from tests import DOMAIN, DEFAULT_WAIT, BROWSER, PORTAL_URL
from selenium.webdriver.chrome.options import Options


class TestUserLogin(LogIn):
    def setUp(self):
        super().setUp()

    def test_log_in_with_valid_credentials(self):
        email = "demo@oxmaint.com"
        password = "123456"
        self.log_in(email, password)
        self.wait.until(EC.url_to_be(PORTAL_URL))

    def test_log_in_with_invalid_email_and_password(self):
        email = "example@gmail.com"
        password = "00000"
        self.log_in(email, password)
        assert (self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='__text2']"))).text ==
                "You are not an authorised user! please check email or password!")
        self.browser.find_element(By.XPATH, "//div[@id='__error0-footer']//button[1]").click()


if __name__ == '__main__':
    unittest.main()
