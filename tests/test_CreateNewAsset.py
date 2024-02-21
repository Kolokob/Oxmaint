import time

from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fixtures.create_asset_fixture import CreateAssetFixture

fake = Faker()


class TestAssignAutoGen(CreateAssetFixture):

    def test_create_new_asset(self):
        super().create_new_asset()

