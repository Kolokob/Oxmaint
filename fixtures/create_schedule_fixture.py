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
one_day_earlier = now - timedelta(days=1)
formatted_date_one_day_earlier = one_day_earlier.strftime("%d-%b-%Y")


class CreateSchedule(AdminLoginFixture):

    def create_schedule(self):
        WebDriverWait(self.browser, 15).until(EC.invisibility_of_element((By.ID, "sap-ui-blocklayer-popup")))
        self.browser.find_element(By.XPATH, "//a[@id='__item425-a']").click()
        self.browser.find_element(By.XPATH, "//span[contains(text(),'Service Schedule')]").click()
        self.browser.find_element(By.XPATH, "//bdi[@id='__button57-BDI-content']").click()

        # Schedule Title
        WebDriverWait(self.browser, 1500).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='__input61-inner']"))).click()
        WebDriverWait(self.browser, 1500).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='__input61-inner']"))).send_keys("Test service schedule")

        # Asset Number
        WebDriverWait(self.browser, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='__input62-inner']"))).click()
        WebDriverWait(self.browser, 300).until(
            EC.element_to_be_clickable((By.XPATH, "//ul[@id='__dialog25-list-listUl']//li[1]"))).click()

        # Last Service Meter Reading
        WebDriverWait(self.browser, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='__input63-inner']")))
        self.browser.find_element(By.XPATH, "//input[@id='__input63-inner']").send_keys(random.randint(1, 500))

        # Intervals
        self.browser.find_element(By.XPATH, "//input[@id='__input65-inner']").send_keys(2)

        # Select "Every" in Intervals
        self.browser.find_element(By.XPATH, "//div[@id='__box82-CbBg']").click()
        self.browser.find_element(By.XPATH, "//input[@id='__input66-inner']").click()
        self.browser.find_element(By.XPATH, "//input[@id='__input66-inner']").send_keys(1)

        # Assign to:
        self.browser.find_element(By.XPATH, "//input[@id='__input69-inner']").click()
        self.browser.find_element(By.XPATH, "//ul[@id='__dialog26-list-listUl']//li[2]").click()

        # Automatically_Generate_WO
        self.browser.find_element(By.XPATH, "//div[@id='__box83-CbBg']").click()

        # Task
        self.browser.find_element(By.XPATH, "//span[@id='__button186-img']").click()
        WebDriverWait(self.browser, 15).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='__dialog27-scroll']//div//input"))).send_keys(
            "Check temperature")
        self.browser.find_element(By.XPATH, "//bdi[@id='__button193-BDI-content']").click()

        # Last Service Date
        self.browser.find_element(By.XPATH, "//input[@id='__picker14-inner']").click()
        self.browser.find_element(By.XPATH, "//input[@id='__picker14-inner']").send_keys(formatted_date_one_day_earlier)

        # Set Schedule
        self.browser.find_element(By.XPATH, "//span[@id='__button190-content']").click()
