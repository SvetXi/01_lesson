from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        basket = self.driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
        basket.click()
        checkout = self.driver.find_element(By.XPATH, "//*[@id='checkout']")
        checkout.click()
