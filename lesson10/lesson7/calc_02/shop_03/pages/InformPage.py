from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class InformPage:
    def __init__(self, driver):
        """
        Инициализация страницы ввода информации.
        :param driver: WebDriver - экземпляр драйвера браузера.
        """
        self.driver = driver

    @allure.step("Заполнение информации и переход к следующему шагу")
    def inform(self) -> None:
        """
        Заполняет поля формы (имя, фамилия, почтовый индекс) и переходит к следующему шагу.
        :return: None
        """
        with allure.step("Заполнение поля 'Имя'"):
            first_name = self.driver.find_element(By.CSS_SELECTOR, "input[name='firstName']")
            first_name.send_keys("Анна")

        with allure.step("Заполнение поля 'Фамилия'"):
            last_name = self.driver.find_element(By.CSS_SELECTOR, "input[name='lastName']")
            last_name.send_keys("Кузнецова")

        with allure.step("Заполнение поля 'Почтовый индекс'"):
            zp_code = self.driver.find_element(By.CSS_SELECTOR, "input[name='postalCode']")
            zp_code.send_keys("296012")

        with allure.step("Нажатие кнопки 'Продолжить'"):
            cont = self.driver.find_element(By.CSS_SELECTOR, "input[class='submit-button btn btn_primary cart_button btn_action']")
            cont.click()
