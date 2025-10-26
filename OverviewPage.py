from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver


class OverviewPage:

    def __init__(self, driver):
        self.driver = driver

    def overview(self):
        total = self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        print(total)

    def assert_sum(self):
        total = self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        print(total)
        assert total == 'Total: $58.29'
