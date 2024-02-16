import random
import time
import unittest

from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from fixtures.admin_login_fixture import AdminLoginFixture
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

now = datetime.now()
one_day_earlier = now - timedelta(days=2)
formatted_date_one_day_earlier = one_day_earlier.strftime("%d-%b-%Y")


class CreateWorkOrder(AdminLoginFixture):

    def create_work_order(self):
        # Open "Creation" Work Order
        WebDriverWait(self.browser, 15).until(EC.invisibility_of_element((By.ID, "sap-ui-blocklayer-popup")))
        self.browser.find_element(By.XPATH, "//a[@id='__item425-a']").click()
        self.browser.find_element(By.XPATH, "//span[contains(text(),'Workorder')]").click()
        self.browser.find_element(By.XPATH, "//div[@id='__table8']//bdi[contains(text(), 'Create Workorder')]").click()

        # Title
        self.browser.find_element(By.XPATH, "//div[@id='__container1--Grid-wrapperfor-__input22']//input").click()
        self.browser.find_element(By.XPATH, "//div[@id='__container1--Grid-wrapperfor-__input22']//input").send_keys("Very Meaningful Title")

        # Asset Number
        self.browser.find_element(By.XPATH, "//input[@placeholder='Select Asset from inventory list']").click()

        # TODO: Continue working on this test
