from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """
    Класс для работы со страницей авторизации на сайте Saucedemo.
    """

    def __init__(self, driver):
        """
        Инициализация страницы авторизации.
        :param driver: WebDriver, экземпляр драйвера для управления браузером.
        """
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/')

    def login(self):
        """
        Выполняет авторизацию на сайте.
        Вводит логин и пароль, затем нажимает кнопку входа.
        """
        username = self.driver.find_element(By.CSS_SELECTOR, "input[name='user-name']")
        username.send_keys("standard_user")
        password = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password.send_keys("secret_sauce")
        login = self.driver.find_element(By.CSS_SELECTOR, "input#login-button")
        login.click()
