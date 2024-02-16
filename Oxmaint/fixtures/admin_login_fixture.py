import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fixtures.base_fixture import OxmaintFixture
from tests import BASE_URL


class AdminLoginFixture(OxmaintFixture):
    def setUp(self):
        super().setUp()

        self.browser.find_element(By.XPATH, "//input[@id='email']").send_keys('demo@oxmaint.com')
        self.browser.find_element(By.XPATH, "//input[@id='password']").send_keys('123456')
        self.browser.find_element(By.XPATH, "//button[@id='Login_with_Email']").click()
        self.wait.until(EC.url_changes(f'{BASE_URL}/portal.html'))
