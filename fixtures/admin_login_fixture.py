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

    def change_language(self, language):
        WebDriverWait(self.browser, 15).until(EC.invisibility_of_element((By.ID, "sap-ui-blocklayer-popup")))
        self.browser.find_element(By.XPATH, "//div[@id='__box1']//span").click()
        self.browser.find_element(By.XPATH,
                                  f"//ul[starts-with(@id, '__box') and contains(@id, '-popup-list-listUl')]//li/div/div/div[contains(text(), '{language.capitalize()}')]").click()

