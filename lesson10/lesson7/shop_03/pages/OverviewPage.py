from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OverviewPage:
    """
    Класс для работы со страницей итоговой информации о заказе.
    """

    def __init__(self, driver):
        """
        Инициализация страницы итоговой информации.
        :param driver: WebDriver, экземпляр драйвера для управления браузером.
        """
        self.driver = driver

    def overview(self):
        """
        Получает итоговую сумму заказа и выводит её в консоль.
        """
        total = self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        print(total)

    def assert_sum(self):
        """
        Проверяет, что итоговая сумма заказа соответствует ожидаемому значению.
        """
        total = self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        print(total)
        assert total == 'Total: $58.29', f"Ожидаемая сумма: 'Total: $58.29', фактическая сумма: {total}"
