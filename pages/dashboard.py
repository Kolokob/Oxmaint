import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests import BASE_URL, DEFAULT_WAIT


class LoginPage:

    PAGE_URL = f"{BASE_URL}/login.html"
    PAGE_HEADER = 'LOGIN Panel'

    def __init__(self, browser: WebDriver, user_name, password, first_name):
        self.first_name = first_name
        self.browser = browser
        self.user_name = user_name
        self.password = password
        self.wait = WebDriverWait(self.browser, DEFAULT_WAIT)

    def authenticate(self):
        self.browser.find_element(By.ID, 'txtUsername').send_keys(self.user_name)
        self.browser.find_element(By.ID, 'txtPassword').send_keys(self.password)
        self.browser.find_element(By.ID, 'btnLogin').click()
        self.wait.until(EC.url_changes(f'{BASE_URL}/login.html'))

    def go_to_page(self):
        self.browser.get(self.PAGE_URL)

    def get_message(self):
        return self.browser.find_element(By.ID, "spanMessage").text