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
    delay_input.send_keys("50")

    # Нажимаем кнопки: 7 + 8 =
    driver.find_element(By.XPATH, "//span[contains(@class, 'btn') and text()='7']").click()
    driver.find_element(By.XPATH, "//span[contains(@class, 'btn') and text()='+']").click()
    driver.find_element(By.XPATH, "//span[contains(@class, 'btn') and text()='8']").click()
    driver.find_element(By.XPATH, "//span[contains(@class, 'btn') and text()='=']").click()


    # Ожидаем текст "15" в поле с результатом (input#result)
    screen = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "screen")))
    value = screen.text

    assert value, "Результат не равен 15 после 45 секунд"
