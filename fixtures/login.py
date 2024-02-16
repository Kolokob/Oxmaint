import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from lib.browser import get_browser
from tests import DOMAIN, DEFAULT_WAIT, BROWSER, PORTAL_URL
from selenium.webdriver.support.wait import WebDriverWait
from fixtures.base_fixture import OxmaintFixture


class LogIn(OxmaintFixture):

    def setUp(self):
        super().setUp()
        self.wait = WebDriverWait(self.browser, DEFAULT_WAIT)

    def log_in(self, email, password):
        self.browser.find_element(By.ID, "email").send_keys(email)
        self.browser.find_element(By.ID, "password").send_keys(password)
        self.browser.find_element(By.ID, "Login_with_Email").click()

