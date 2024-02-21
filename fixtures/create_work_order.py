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
one_week_later = now + timedelta(weeks=1)
formatted_date_one_week_later = one_week_later.strftime("%d-%b-%Y %I:%M %p")


class CreateWorkOrder(AdminLoginFixture):

    def create_work_order(self):
        # Open "Creation" Work Order
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//li[@id='__item425']"))).click()
        self.browser.find_element(By.XPATH, "//span[contains(text(),'Workorder')]").click()
        self.browser.find_element(By.XPATH, "//div[@id='__table8']//bdi[contains(text(), 'Create Workorder')]").click()

        # Title
        self.browser.find_element(By.XPATH, "//div[@id='__container1--Grid-wrapperfor-__input22']//input").click()
        self.browser.find_element(By.XPATH, "//div[@id='__container1--Grid-wrapperfor-__input22']//input").send_keys("Very Meaningful Title")

        # Memo
        self.browser.find_element(By.XPATH, "//textarea[@id='__area1-inner']").click()
        self.browser.find_element(By.XPATH, "//textarea[@id='__area1-inner']").send_keys("Very Meaningful Title")

        # Assigned to
        self.browser.find_element(By.XPATH, "//span[@id='__input21-vhi']").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@id='__dialog27-list-listUl']//li[1]")))
        self.browser.find_element(By.XPATH, "//bdi[contains(text(), 'Select')]").click()

        # Meter Reading
        self.browser.find_element(By.XPATH, "//input[@id='__input7-inner']").click()
        self.browser.find_element(By.XPATH, "//input[@id='__input7-inner']").send_keys(200)

        time.sleep(1000)









        # Asset Number
        self.browser.find_element(By.XPATH, "//input[@placeholder='Select Asset from inventory list']").click()
        self.browser.find_element(By.XPATH, "//td[@id='__item34-__table1-0_cell4']//button").click()





