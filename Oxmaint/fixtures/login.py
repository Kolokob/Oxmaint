import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from tests import BASE_URL
from lib.browser import get_browser
from tests import DOMAIN, DEFAULT_WAIT, BROWSER
from selenium.webdriver.support.wait import WebDriverWait


class LogIn(unittest.TestCase):

    def __init__(self):
        super().__init__()
        self.browser = get_browser(BROWSER)
        self.wait = WebDriverWait(self.browser, DEFAULT_WAIT)

    def log_in(self, browser, user_name, password, first_name):
        browser.find_element(By.ID, 'txtUsername').send_keys(user_name)
        browser.find_element(By.ID, 'txtPassword').send_keys(password)
        browser.find_element(By.ID, 'btnLogin').click()
        self.wait.until(EC.url_changes(f'{BASE_URL}/auth/login'))
        self.assertEqual(browser.find_element(By.XPATH, "//a[@id='welcome']").text, f'Welcome {first_name}')
