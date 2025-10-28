
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    edge_driver_path = r"C:\Users\Khism\Downloads\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    driver.maximize_window()
    yield driver
    driver.quit()
    
    def driver():

    # Автоматическое скачивание и установка драйвера Edge
    edge_driver_path = r"C:\Users\Khism\Downloads\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path)) 
    driver.maximize_window()
    yield driver
    driver.quit()
def test_fill_form_and_check_colors(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    wait = WebDriverWait(driver, 10)

    # Заполнение полей
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.ID, "email").send_keys("test@skypro.com")
    driver.find_element(By.ID, "phone").send_keys("+7985899998787")
    # Zip code оставить пустым - не заполняем
    driver.find_element(By.ID, "city").send_keys("Москва")
    driver.find_element(By.ID, "country").send_keys("Россия")
    driver.find_element(By.ID, "job-position").send_keys("QA")
    driver.find_element(By.ID, "company").send_keys("SkyPro")

    # Нажать Submit
    driver.find_element(By.ID, "submit-button").click()

    # Ожидания, что поля подсветятся (именно по style или классу)
    def has_green_border(el):
        border_color = el.value_of_css_property("border-color")
        return "rgb(40, 167, 69)" in border_color or "green" in border_color

    def has_red_border(el):
        border_color = el.value_of_css_property("border-color")
        return "rgb(220, 53, 69)" in border_color or "red" in border_color

    # Ждем, что zip код подсветится красным
    zip_elem = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
    wait.until(lambda d: has_red_border(zip_elem))

    # Проверяем, что zip код подсвечен красным
    assert has_red_border(zip_elem), "Zip code поле не подсвечено красным"

    # Проверяем остальные поля подсвечены зеленым (кроме zip code)
    ids_green = [
        "first-name", "last-name", "address", "email", "phone",
        "city", "country", "job-position", "company"
    ]
    for field_id in ids_green:
        elem = driver.find_element(By.ID, field_id)
        assert has_green_border(elem), f"Поле {field_id} не подсвечено зеленым"
