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

fake = Faker()
asset_categories = [
    "Vehicles",
    "Computer Equipment",
    "Furniture",
    "Industrial Equipment",
    "Electronics",
    "Real Estate",
    "Machinery",
    "Office Supplies",
    "Software",
    "Artwork"
]
model_list = [
    "ProMax 2000",
    "UltraX 500",
    "AlphaWave 3",
    "Solaris Z10",
    "Quantum 6R",
    "Galaxy S12",
    "Delta 4G",
    "Orion P8",
    "Eclipse 9000",
    "Neptune X2"
]
year = randint(2017, 2023)
month = randint(1, 12)
day = randint(1, 28)

today = datetime.now()

week_ago = today - timedelta(days=7)

random_seconds = random.randint(0, int((today - week_ago).total_seconds()))
random_datee = week_ago + timedelta(seconds=random_seconds)
random_date = datetime(year, month, day)  # selected 28 to avoid problems with February

first_day_of_last_month = today.replace(day=1) - timedelta(days=1)
last_day_of_last_month = first_day_of_last_month.replace(day=1)
random_date_in_past_month = last_day_of_last_month + timedelta(days=random.randint(1, first_day_of_last_month.day))
three_months_later = today + timedelta(days=90)
random_date_in_next_three_months = today + timedelta(days=random.randint(0, (three_months_later - today).days))

formatted_random_date_in_past_month = random_date.strftime('%d-%b-%Y')
formatted_date = random_date.strftime('%d-%b-%Y')
formatted_random_date = random_datee.strftime('%d-%b-%Y')
formatted_random_date_in_next_three_months = random_date_in_next_three_months.strftime('%d-%b-%Y')

images_file_path = "/var/jenkins_home/workspace/Python build and test demo/photos"
files = os.listdir(images_file_path)
photo_files = [file for file in files if file.endswith('.jpg')]
random_photo_file = random.choice(photo_files)
full_photo_path = os.path.join(images_file_path, random_photo_file)


class CreateAssetFixture(AdminLoginFixture):

    def create_new_asset(self):
        self.random_asset_number = random.randint(1, 4500)
        self.random_asset_name = fake.word()
        self.random_asset_category = random.choice(asset_categories)
        self.random_asset_model = random.choice(model_list)
        self.random_meter_reading = random.randint(1, 500)
        self.random_asset_status = f"//div[@aria-labelledby='__text3']/div//li[{random.randint(1, 7)}]"

        # Go to assets
        WebDriverWait(self.browser, 10).until(
            EC.invisibility_of_element((By.ID, "sap-ui-blocklayer-popup"))
        )
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='__navigation0-Flexible-Content']/ul/li[5]"))).click()
        self.browser.find_element(By.XPATH, "(//span[contains(text(),'Assets')])[3]").click()

        # Go to creation of new asset
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//bdi[@id='__button0-BDI-content']"))).click()

        # Asset Number
        self.browser.find_element(By.XPATH, "//input[@id='__input60-inner']").click()
        self.browser.find_element(By.XPATH, "//input[@id='__input60-inner']").send_keys(self.random_asset_number)

        # Asset Name
        self.browser.find_element(By.XPATH, "//input[@id='__input61-inner']").click()
        self.browser.find_element(By.XPATH, "//input[@id='__input61-inner']").send_keys(self.random_asset_name)

        # Asset Category
        self.browser.find_element(By.XPATH, "//input[@id='__input62-inner']").click()
        self.browser.find_element(By.XPATH, "//input[@id='__input62-inner']").send_keys(self.random_asset_category)

        # Asset Model
        self.browser.find_element(By.XPATH, "//input[@id='__input64-inner']").click()
        self.browser.find_element(By.XPATH, "//input[@id='__input64-inner']").send_keys(self.random_asset_model)

        # Meter Reading
        self.browser.find_element(By.XPATH, "//input[@id='__input65-inner']").click()
        self.browser.find_element(By.XPATH, "//input[@id='__input65-inner']").send_keys(self.random_meter_reading)

        # Asset Status
        try:
            time.sleep(1)
            self.browser.find_element(By.XPATH, "(//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][1]//div[13]//span)[1]").click()
            time.sleep(1)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.random_asset_status))).click()
        except ElementClickInterceptedException or TimeoutException:
            self.browser.find_element(By.XPATH, "(//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][1]//div[13]//span)[1]").click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.random_asset_status))).click()

        # Inventory#
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][1]//div[15]//input").click()
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][1]//div[15]//input").send_keys("8462919000/YQ32")

        # Asset Utilization Goal
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][1]//div[17]//input").click()
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][1]//div[17]//input").send_keys(
            "Maximize machinery uptime "
            "to achieve a 20% increase "
            "in production efficiency by "
            "the end of the year.")

        # Site Project
        try:
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, "(//div[@id='sap-ui-static']//span[@role='button'])[3]"))).click()
            self.browser.find_element(By.XPATH, f"(//div[starts-with(@id, '__box') and contains(@id, '-popup-cont')])[2]//ul//li[{random.randint(1, 7)}]").click()

        except TimeoutException:
            self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "(//div[@id='sap-ui-static']//span[@role='button'])[3]"))).click()
            self.browser.find_element(By.XPATH,
                                      f"(//div[starts-with(@id, '__box') and contains(@id, '-popup-cont')])[2]//ul//li[{random.randint(1, 7)}]").click()
        finally:
            print("Site Project could not be set up, please try again")


        # Business Unit
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][3]//div[4]//input").click()
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][3]//div[4]//input").send_keys(
            "Optimize asset use to "
            "enhance productivity and "
            "reduce maintenance costs.")

        # Assert Value
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][3]//div[6]//input").click()
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][3]//div[6]//input").send_keys(
            "$50,000")

        # Purchase Date
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][3]//div[8]//input").click()
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][3]//div[8]//input").send_keys(
            formatted_date)

        # Warranty Date
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][3]//div[10]//input").click()
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][3]//div[10]//input").send_keys(
            formatted_random_date)

        # Required Geo Location while Inspection CheckBox
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][3]//div[12]/div/div").click()

        # Assign Inspection Form
        self.browser.find_element(By.XPATH, "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][3]//div[13]//div//button/span").click()
        self.browser.find_element(By.XPATH,
                                  "(//div[starts-with(@id, '__dialog') and substring(@id, string-length(@id) - string-length('-list') + 1) = '-list']//ul//li[1]/div/div)[1]").click()
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__dialog') and contains(@id, '-dialog-footer')]/button[1]").click()

        # Year
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][2]/div/div[2]").click()
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][2]/div/div[2]//input").send_keys(
            2024)

        # Chassis Number
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][2]//div[4]").click()
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][2]//div[4]//input").send_keys(
            "A3234JT")

        # Manufacture
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][2]//div[6]").click()
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][2]//div[6]//input").send_keys(
            "Additive manufacturing")

        # License Plate
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][2]//div[8]").click()
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][2]//div[8]//input").send_keys(
            "XYZ01234")

        # Last Service Reading
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][2]//div[10]").click()
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][2]//div[10]//input").send_keys(
            random.randint(130, 400))

        # Last Service Date
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][2]//div[12]").click()
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][2]//div[12]//input").send_keys(
            formatted_random_date_in_past_month)

        # Registration State
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][2]//div[14]").click()
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][2]//div[14]//input").send_keys(
            "CA")

        # Registration Exp Date
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][2]//div[16]").click()
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][2]//div[16]//input").send_keys(
            formatted_random_date_in_next_three_months)

        # Operator name
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][4]/div/div[2]").click()
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][4]/div/div[2]//input").send_keys(
            fake.name())

        # Maintenance Priority
        self.browser.find_element(By.XPATH,
                                  "(//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][4]/div/div[4]//span)[1]").click()
        self.browser.find_element(By.XPATH,
                                  f"(//ul[starts-with(@id, '__box') and contains(@id, '-popup-list-listUl')])[3]//li[{random.randint(1, 5)}]").click()

        # Ownership Mode
        self.browser.find_element(By.XPATH,
                                  "(//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][4]/div/div[6]//span)[1]").click()
        self.browser.find_element(By.XPATH,
                                  f"(//ul[starts-with(@id, '__box') and contains(@id, '-popup-list-listUl')])[4]//li[{random.randint(1, 3)}]").click()

        # Asset Note
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][4]/div/div[8]").click()
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][4]/div/div[8]//textarea").send_keys(
            "Regular maintenance ensures optimal performance and longevity. Consider future upgrades for enhanced efficiency.")

        # Asset Image
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][4]/div/div[10]//button/span").click()
        self.browser.find_element(By.XPATH, "//input[@type='file']").send_keys(full_photo_path)
        self.browser.find_element(By.XPATH,
                                  "(//footer[@class='sapMDialogFooter'])[2]//bdi[contains(text(), 'Upload')]").click()

        # GPS Enabled
        self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                    "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][4]/div/div[12]/div/div"))).click()

        # Device ID
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][4]/div/div[14]").click()
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][4]/div/div[14]//input").send_keys(
            random.randint(50, 100))

        # GPS Asset ID
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][4]/div/div[16]").click()
        self.browser.find_element(By.XPATH,
                                  "//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][4]/div/div[16]//input").send_keys(
            str(random.randint(400, 800)) + "FG")

        self.wait.until(
            EC.presence_of_element_located((By.XPATH,
                                            "(//div[starts-with(@id, '__form') and contains(@id, '--Grid-wrapperfor-__container') and contains(@id, '--Grid')][1]//div[13]//span)[1]"))).click()
        self.random_asset_status_2 = self.browser.find_element(By.XPATH, self.random_asset_status + "/div/div/div").text

        # Add Asset
        self.browser.find_element(By.XPATH,
                                  "//footer[@class='sapMDialogFooter']//bdi[contains(text(), 'Add Asset')]").click()
        time.sleep(2)

        # Check that just created asset actually created and all the info matches to input info
        actual_asset_number = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//tbody[@class='sapMListItems sapMTableTBody']//tr[1]//td[@data-sap-ui-column='__column2']//bdi"))).text
        actual_asset_category = self.browser.find_element(By.XPATH, "//tbody[@class='sapMListItems sapMTableTBody']//tr[1]//td[@data-sap-ui-column='__column3']//bdi").text
        actual_asset_name = self.browser.find_element(By.XPATH, "//tbody[@class='sapMListItems sapMTableTBody']//tr[1]//td[@data-sap-ui-column='__column4']//bdi").text
        actual_asset_model = self.browser.find_element(By.XPATH, "//tbody[@class='sapMListItems sapMTableTBody']//tr[1]//td[@data-sap-ui-column='__column6']//bdi").text
        actual_asset_meter = self.browser.find_element(By.XPATH, "//tbody[@class='sapMListItems sapMTableTBody']//tr[1]//td[@data-sap-ui-column='__column7']//bdi").text
        actual_asset_status = self.browser.find_element(By.XPATH, "//tbody[@class='sapMListItems sapMTableTBody']//tr[1]//td[@data-sap-ui-column='__column8']//span/span").text

        assert int(actual_asset_number) == int(self.random_asset_number)
        assert actual_asset_category == self.random_asset_category
        assert actual_asset_name == self.random_asset_name
        assert actual_asset_model == self.random_asset_model
        assert int(actual_asset_meter) == int(self.random_meter_reading)
        assert actual_asset_status.lower() == self.random_asset_status_2.lower()
