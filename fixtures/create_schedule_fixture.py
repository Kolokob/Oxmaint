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


class CreateSchedule(AdminLoginFixture):

    def create_schedule(self):
        # Open "Creation" Schedule
        WebDriverWait(self.browser, 15).until(EC.invisibility_of_element((By.ID, "sap-ui-blocklayer-popup")))
        self.browser.find_element(By.XPATH, "//div[@id='__navigation0-Flexible-Content']/ul/li[2]").click()
        self.browser.find_element(By.XPATH, "//span[contains(text(),'サービススケジュール')]").click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//bdi[@id='__button57-BDI-content']"))).click()

        # Schedule Title
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']")))
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][1]//div[4]"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][1]//div[4]//input"))).send_keys("試験サービススケジュール")

        # Asset Number
        WebDriverWait(self.browser, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][1]//div[7]//span"))).click()
        WebDriverWait(self.browser, 300).until(
            EC.element_to_be_clickable((By.XPATH, "//ul[@id='__dialog25-list-listUl']//li[1]"))).click()

        # Last Service Meter Reading
        WebDriverWait(self.browser, 15).until(
            EC.presence_of_element_located((By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][1]//div[11]//input"))).click()
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][1]//div[11]//input").send_keys(random.randint(1, 500))

        # Last Service Date
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][1]//div[13]//input").click()
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][1]//div[13]//input").send_keys(formatted_date_one_day_earlier)

        # Intervals
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][3]//div[4]//div[2]//input").send_keys(10)

        # Select "Every" in Intervals
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][3]//div[6]//div[1]//div[1]/div/div").click()
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][3]//div[6]//div[1]//div[3]//input").click()
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][3]//div[6]//div[1]//div[3]//input").send_keys(10)

        # Assign to:
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][5]//div[2]/div/div//div[2]").click()
        self.browser.find_element(By.XPATH, "//ul[@id='__dialog26-list-listUl']//li[2]").click()

        # Automatically_Generate_WO
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][5]//div[4]/div/div").click()

        # Task
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][2]//div[5]//div[last()]/div//button").click()
        WebDriverWait(self.browser, 15).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='__dialog27-scroll']//div//input"))).send_keys(
            "温度チェック")
        self.browser.find_element(By.XPATH, "(//div[starts-with(@id, '__dialog') and contains(@id, '-footer')])[2]//bdi[contains(text(), '追加')]").click()

        # Notify Before
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][4]//div[3]//input").click()
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][4]//div[3]//input").clear()
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][4]//div[3]//input").send_keys(3)

        # Set Schedule
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__dialog') and contains(@id, '-footer')]/button[1]/span").click()
