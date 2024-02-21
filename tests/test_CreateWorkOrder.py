import time
import unittest

from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fixtures.create_work_order_fixture import CreateWorkOrder

fake = Faker()


class TestCreateWorkOrder(CreateWorkOrder):

    def test_create_work_order(self):
        super().create_work_order()
