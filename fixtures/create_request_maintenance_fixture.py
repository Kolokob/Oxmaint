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
class CreateRequestMaintenance(AdminLoginFixture):

    def wait_to_be_text(self, xpath):
        element = self.browser.find_element(By.XPATH, xpath).text
        while element == "":
            time.sleep(1)
            element = self.browser.find_element(By.XPATH, xpath).text
        return element


    def request_maintenance(self):
        WebDriverWait(self.browser, 15).until(EC.invisibility_of_element((By.ID, "sap-ui-blocklayer-popup")))
        self.browser.find_element(By.XPATH, "//div[@id='__navigation0-Flexible-Content']/ul/li[2]").click()
        self.browser.find_element(By.XPATH, "//span[contains(text(),'Request Maintenance')]").click()
        self.browser.find_element(By.XPATH, "//bdi[contains(text(), 'Create Request')] ").click()

        # Noting WorkOrder Number
        self.work_order_number = self.wait_to_be_text("//span[@id='wo_number-inner']")

        # Title
        self.browser.find_element(By.XPATH, "//div[@id='__container1--Grid-wrapperfor-__input22']//input").click()
        self.title = fake.name()
        self.browser.find_element(By.XPATH, "//div[@id='__container1--Grid-wrapperfor-__input22']//input").send_keys(self.title)

        # Note Priority
        time.sleep(1)
        self.request_priority = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid')][1]//div[6]//span/span[2]"))).text

        # Memo
        self.browser.find_element(By.XPATH, "//textarea[@id='__area1-inner']").click()
        self.memo = fake.text()
        self.browser.find_element(By.XPATH, "//textarea[@id='__area1-inner']").send_keys(self.memo)

        # Assigned to
        self.browser.find_element(By.XPATH, "//span[@id='__input21-vhi']").click()
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[starts-with(@id, '__dialog') and contains(@id, '-list')]//li[1]")))
        self.browser.find_element(By.XPATH, "//bdi[contains(text(), 'Select')]").click()

        # Meter Reading
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='__input7-inner']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='__input7-inner']"))).send_keys(200)

        # Asset Number
        self.browser.find_element(By.XPATH,
                                  "(//div[starts-with(@id, '__form') and contains(@id, '--Grid')][2]//div[2]//span)[1]").click()
        self.asset_number = self.wait_to_be_text("(//*[starts-with(@id, '__table') and contains(@id, '-tblBody')]//tr[1]//td[2]//bdi)[1]")

        self.browser.find_element(By.XPATH,
                                  "//*[starts-with(@id, '__table') and contains(@id, '-tblBody')]//tr[1]//td[last()-2]/button/span").click()

        # Task Detail
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//section[starts-with(@id, '__section')][2]/div[2]//button[2]/span"))).click()
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__dialog') and contains(@id, '-scrollCont')]//div[2]//input").click()
        # Note Task Status
        self.task_status = self.browser.find_element(By.XPATH,
                                                     "//div[starts-with(@id, '__dialog') and contains(@id, '-scrollCont')]//div[4]//span/span[2]").text
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__dialog') and contains(@id, '-scrollCont')]//div[2]//input").send_keys("TASK 1")
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__dialog') and contains(@id, '-footer')]//button[1]/span").click()

        # Create WorkOrder
        time.sleep(3)
        self.browser.find_element(By.XPATH,
                                  "//bdi[starts-with(@id, '__button') and contains(@id, '-BDI-content')][contains(text(), 'Create Request')]").click()

        time.sleep(3)

        assert self.browser.find_element(By.XPATH,
                                         "(//*[starts-with(@id, '__table') and contains(@id, '-tblBody')]//tr[1]//td[3]//bdi)[1]").text == self.work_order_number

        assert self.browser.find_element(By.XPATH,
                                         "(//*[starts-with(@id, '__table') and contains(@id, '-tblBody')]//tr[1]//td[3]//bdi)[2]").text == self.title

        assert self.browser.find_element(By.XPATH,
                                         "(//*[starts-with(@id, '__table') and contains(@id, '-tblBody')]//tr[1]/td[5]//bdi)[1]").text == self.asset_number

        assert self.browser.find_element(By.XPATH,
                                         "//*[starts-with(@id, '__table') and contains(@id, '-tblBody')]//tr[1]/td[6]//span[1]/span").text == "Requested".upper()

        assert self.browser.find_element(By.XPATH,
                                         "//*[starts-with(@id, '__table') and contains(@id, '-tblBody')]//tr[1]/td[7]//span/span").text == self.request_priority.upper()

        assert self.browser.find_element(By.XPATH,
                                         "//*[starts-with(@id, '__table') and contains(@id, '-tblBody')]//tr[1]/td[8]//span/span[2]/bdi").text == "0"
        self.actual_memo = self.browser.find_element(By.XPATH,
                                         "//*[starts-with(@id, '__table') and contains(@id, '-tblBody')]//tr[1]/td[9]//span//bdi").text

        assert self.actual_memo == self.memo

