from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class FormPage:
    def __init__(self, driver):
        """
        Инициализация страницы формы.
        :param driver: WebDriver - экземпляр драйвера браузера.
        """
        self.driver = driver
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    @allure.step("Заполнение формы данными")
    def complete_the_form(self) -> None:
        """
        Заполняет все поля формы тестовыми данными.
        :return: None
        """
        with allure.step("Заполнение поля 'Имя'"):
            first_name = self.driver.find_element(By.CSS_SELECTOR, "input[name='first-name']")
            first_name.send_keys("Иван")

        with allure.step("Заполнение поля 'Фамилия'"):
            last_name = self.driver.find_element(By.CSS_SELECTOR, "input[name='last-name']")
            last_name.send_keys("Петров")

        with allure.step("Заполнение поля 'Адрес'"):
            address = self.driver.find_element(By.CSS_SELECTOR, "input[name='address']")
            address.send_keys("Ленина, 55-3")

        with allure.step("Заполнение поля 'Почтовый индекс' (оставлено пустым)"):
            zip_code = self.driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']")
            zip_code.send_keys("")

        with allure.step("Заполнение поля 'Город'"):
            city = self.driver.find_element(By.CSS_SELECTOR, "input[name='city']")
            city.send_keys("Москва")

        with allure.step("Заполнение поля 'Страна'"):
            country = self.driver.find_element(By.CSS_SELECTOR, "input[name='country']")
            country.send_keys("Россия")

        with allure.step("Заполнение поля 'E-mail'"):
            email = self.driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']")
            email.send_keys("test@skypro.com")

        with allure.step("Заполнение поля 'Телефон'"):
            phone_number = self.driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
            phone_number.send_keys("+7985899998787")

        with allure.step("Заполнение поля 'Должность'"):
            job_position = self.driver.find_element(By.CSS_SELECTOR, "input[name='job-position']")
            job_position.send_keys("QA")

        with allure.step("Заполнение поля 'Компания'"):
            company = self.driver.find_element(By.CSS_SELECTOR, "input[name='company']")
            company.send_keys("SkyPro")

    @allure.step("Нажатие кнопки 'Submit'")
    def sublime_click(self) -> None:
        """
        Нажимает кнопку отправки формы.
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    @allure.step("Проверка, что поле 'Почтовый индекс' подсвечено красным")
    def zip_code_red(self) -> None:
        """
        Проверяет, что поле 'Почтовый индекс' подсвечено красным цветом.
        :return: None
        """
        alert_danger_color = "rgba(248, 215, 218, 1)"
        zip_code = self.driver.find_element(By.CSS_SELECTOR, "#zip-code")
        color_zip = zip_code.value_of_css_property("background-color")
        assert color_zip == alert_danger_color, f"Expected {alert_danger_color}, but got {color_zip}"

    @allure.step("Проверка, что остальные поля подсвечены зеленым")
    def other_green(self) -> None:
        """
        Проверяет, что все остальные поля формы подсвечены зеленым цветом.
        :return: None
        """
        fields_to_check = ["first-name", "last-name", "address", "e-mail", "phone",
                           "city", "country", "job-position", "company"]
        for field_name in fields_to_check:
            with allure.step(f"Проверка поля '{field_name}'"):
                field = WebDriverWait(self.driver,10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, f"div.alert.py-2.alert-success[id='{field_name}']")))
                background_color = field.value_of_css_property("background-color")
                assert background_color == "rgba(209, 231, 221, 1)", \
                    f"Field {field_name} has incorrect background color: {background_color}"
