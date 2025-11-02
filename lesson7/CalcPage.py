from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcPage:
    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.
        :param driver: WebDriver - экземпляр драйвера браузера.
        """
        self.driver = driver
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    @allure.step("Установка задержки вычислений")
    def delay(self) -> None:
        """
        Устанавливает задержку вычислений на 45 секунд.
        :return: None
        """
        delay = self.driver.find_element(By.CSS_SELECTOR, "input[id='delay']")
        delay.clear()
        delay.send_keys("45")

    @allure.step("Выполнение вычисления: 7 + 8")
    def calculator(self) -> None:
        """
        Выполняет вычисление 7 + 8 и ожидает результат.
        :return: None
        """
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()

        WebDriverWait(self.driver, 46).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    @allure.step("Проверка результата вычислений")
    def result(self) -> None:
        """
        Проверяет, что результат вычислений равен 15.
        :return: None
        """
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert int(result) == 15, f"Expected result 15, but got {result}"
        WebDriverWait(self.driver, 46).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    def result(self):
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert int(result) == 15
