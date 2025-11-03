from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:
    def __init__(self, driver):
        """
        Инициализация страницы корзины.
        :param driver: WebDriver - экземпляр драйвера браузера.
        """
        self.driver = driver

    @allure.step("Добавление товаров в корзину и переход к оформлению заказа")
    def cart(self) -> None:
        """
        Добавляет товары в корзину и переходит к оформлению заказа.
        :return: None
        """
        with allure.step("Добавление товара 'Sauce Labs Backpack' в корзину"):
            self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

        with allure.step("Добавление товара 'Sauce Labs Bolt T-Shirt' в корзину"):
            self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

        with allure.step("Добавление товара 'Sauce Labs Onesie' в корзину"):
            self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

        with allure.step("Переход в корзину"):
            basket = self.driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
            basket.click()

        with allure.step("Переход к оформлению заказа"):
            checkout = self.driver.find_element(By.XPATH, "//*[@id='checkout']")
            checkout.click()
