import os
import time
import random
from random import randint
from datetime import datetime, timedelta
from faker import Faker
from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fixtures.admin_login_fixture import AdminLoginFixture


class ChangeLanguageFixture(AdminLoginFixture):

    def change_language(self, language: str):
        super().setUp()
        WebDriverWait(self.browser, 15).until(EC.invisibility_of_element((By.ID, "sap-ui-blocklayer-popup")))
        self.browser.find_element(By.XPATH, "//div[@id='__box1']//span").click()
        self.browser.find_element(By.XPATH,
                                  f"//ul[starts-with(@id, '__box') and contains(@id, '-popup-list-listUl')]//li/div/div/div[contains(text(), '{language.capitalize()}')]").click()
