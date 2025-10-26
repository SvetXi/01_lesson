from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver


class  FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    def complete_the_form(self):
        first_name = self.driver.find_element(By.CSS_SELECTOR, "input[name='first-name']")
        first_name.send_keys("Иван")

        last_name = self.driver.find_element(By.CSS_SELECTOR, "input[name='last-name']")
        last_name.send_keys("Петров")

        address = self.driver.find_element(By.CSS_SELECTOR, "input[name='address']")
        address.send_keys("Ленина, 55-3")

        zip_code = self.driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']")
        zip_code.send_keys("")

        city = self.driver.find_element(By.CSS_SELECTOR, "input[name='city']")
        city.send_keys("Москва")

        country = self.driver.find_element(By.CSS_SELECTOR, "input[name='country']")
        country.send_keys("Россия")

        email = self.driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']")
        email.send_keys("test@skypro.com")

        phone_number = self.driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
        phone_number.send_keys("+7985899998787")

        job_position = self.driver.find_element(By.CSS_SELECTOR, "input[name='job-position']")
        job_position.send_keys("QA")

        company = self.driver.find_element(By.CSS_SELECTOR, "input[name='company']")
        company.send_keys("SkyPro")

    def sublime_click(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def zip_code_red(self):
        alert_danger_color = "rgba(248, 215, 218, 1)"
        zip_code = self.driver.find_element(By.CSS_SELECTOR, "#zip-code")
        color_zip = zip_code.value_of_css_property("background-color")
        assert color_zip == alert_danger_color, f"Expected {alert_danger_color}, but got {color_zip}"

    def other_green(self):
        fields_to_check = ["first-name", "last-name", "address", "e-mail", "phone",
                           "city", "country", "job-position", "company"]
        for field_name in fields_to_check:
            field = self.driver.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, f"div.alert.py-2.alert-success[id='{field_name}']")))
            background_color = field.value_of_css_property("background-color")
            assert background_color == "rgba(209, 231, 221, 1)"
