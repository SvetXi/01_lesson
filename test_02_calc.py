import pytest
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = ChromeOptions()
    # Запуск Chrome
    service = ChromeService()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_slow_calc(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    wait = WebDriverWait(driver, 50)  # ожидание чуть больше 45 с

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажимаем кнопки: 7 + 8 =
    driver.find_element(By.CSS_SELECTOR, "button.btn[data-value='7']").click()
    driver.find_element(By.CSS_SELECTOR, "button.btn[data-value='+']").click()
    driver.find_element(By.CSS_SELECTOR, "button.btn[data-value='8']").click()
    driver.find_element(By.CSS_SELECTOR, "button.btn[data-value='=']").click()

    # Ожидаем текст "15" в поле с результатом (input#result)
    result = wait.until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, "input#result"), "15"))

    assert result, "Результат не равен 15 после 45 секунд"
