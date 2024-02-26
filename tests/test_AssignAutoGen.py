import time
import unittest

from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fixtures.create_schedule_fixture import CreateSchedule
from fixtures.change_language_fixture import ChangeLanguageFixture

fake = Faker()
change_language_attr = ChangeLanguageFixture()

class TestAssignAutoGen(CreateSchedule):

    # def test_create_schedule(self):
    #     super().create_schedule()
    #
    #     time.sleep(1)
    #
    #     # Switch to Work Orders
    #     WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(
    #         (By.XPATH, "(//bdi[contains(text(),'Create Workorder')]/ancestor::button)[1]"))).click()
    #     time.sleep(1)
    #     work_order_number = WebDriverWait(self.browser, 15).until(
    #         EC.presence_of_element_located((By.XPATH, "//span[@id='wo_number-inner']"))).text
    #
    #     # Create Work Order
    #     time.sleep(1)
    #     self.browser.find_element(By.XPATH, "//bdi[@id='__button52-BDI-content']").click()
    #
    #     # Check that created work order equals to work order that in work orders list
    #     time.sleep(2)
    #     assert self.browser.find_element(By.XPATH,
    #                                      "(//tbody[@id='__table8-tblBody']//td[3]//bdi)[1]").text == work_order_number

    def test_create_schedule_with_different_language(self):
        super().change_language("Japanese")
        super().create_schedule()

        time.sleep(1)

        # Switch to Work Orders
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'作業命令')]"))).click()
        time.sleep(1)
        work_order_number = WebDriverWait(self.browser, 15).until(
            EC.presence_of_element_located((By.XPATH, "//span[@id='wo_number-inner']"))).text

        # Create Work Order
        time.sleep(1)
        self.browser.find_element(By.XPATH, "//bdi[@id='__button52-BDI-content']").click()

        # Check that created work order equals to work order that in work orders list
        time.sleep(2)
        assert self.browser.find_element(By.XPATH,
                                         "(//tbody[@id='__table8-tblBody']//td[3]//bdi)[1]").text == work_order_number


if __name__ == '__main__':
    unittest.main()
