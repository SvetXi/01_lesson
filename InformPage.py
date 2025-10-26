from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver


class InformPage:

    def __init__(self, driver):
        self.driver = driver

    def inform(self):
        first_name = self.driver.find_element(By.CSS_SELECTOR, "input[name='firstName']")
        first_name.send_keys("Мария")
        last_name = self.driver.find_element(By.CSS_SELECTOR, "input[name='lastName']")
        last_name.send_keys("Ботнарь")
        zp_code = self.driver.find_element(By.CSS_SELECTOR, "input[name='postalCode']")
        zp_code.send_keys("292940")
        cont = self.driver.find_element(By.CSS_SELECTOR, "input[class='submit-button btn btn_primary cart_button btn_action']")
        cont.click()
