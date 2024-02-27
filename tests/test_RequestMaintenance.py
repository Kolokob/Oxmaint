import time
import unittest
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fixtures.create_request_maintenance_fixture import CreateRequestMaintenance

fake = Faker()


class TestCreateRequestMaintenance(CreateRequestMaintenance):

    def test_create_request_maintenance(self):
        super().request_maintenance()
