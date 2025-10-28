import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = EdgeOptions()
    # Запуск браузера Edge
    service = EdgeService()
    driver = webdriver.Edge(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form_fields_validation(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    wait = WebDriverWait(driver, 20)

    # Заполняем форму
    driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    # Zip code оставляем пустым
    driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").clear()
    driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")


    button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    driver.execute_script("arguments[0].scrollIntoView();", button)
    driver.execute_script("arguments[0].click();", button)

    # Проверяем, что поле Zip code подсвечено красным (наличие класса или стилевой окрас)
    zip_field = driver.find_element(By.ID, "zip-code")
    # Ждем появления красного бордера (считаем, что бордер красного цвета — rgb(255, 0, 0))
    # wait.until(lambda d: "red" in zip_field.value_of_css_property("border-color") or
    #                    "rgb(255, 0, 0)" in zip_field.value_of_css_property("border-color"))

    border_zip = zip_field.value_of_css_property("border-color")
    assert "245, 194, 199" in border_zip or "red" in border_zip, "Zip code поле не подсвечено красным"

    # Проверяем остальные поля на зеленый бордер (rgb(40, 167, 69) — bootstrap success)
    # Список остальных полей
    fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
    for field_id in fields:
        field = driver.find_element(By.ID, field_id)
        border = field.value_of_css_property("border-color")
        assert border == "rgb(186, 219, 204)", \
            f"Поле {field} не подсвечено зеленым"