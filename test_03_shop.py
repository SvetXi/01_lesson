import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = FirefoxOptions()
    service = FirefoxService()
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_sauce_demo_purchase(driver):
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Ожидаем загрузку страницы с товарами
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))

    # Добавляем в корзину указанные товары
    items = {
        "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
        "Sauce Labs Bolt T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
        "Sauce Labs Onesie": "add-to-cart-sauce-labs-onesie",
    }
    for button_id in items.values():
        driver.find_element(By.ID, button_id).click()

    # Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart_list")))

    # Нажимаем Checkout
    driver.find_element(By.ID, "checkout").click()
    wait.until(EC.visibility_of_element_located((By.ID, "first-name")))

    # Заполняем форму
    driver.find_element(By.ID, "first-name").send_keys("Имя")
    driver.find_element(By.ID, "last-name").send_keys("Фамилия")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    driver.find_element(By.ID, "continue").click()

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))

    total_elem = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_elem.text  # строка вида: "Total: $58.29"

    assert total_text == "Total: $58.29", f"Итоговая сумма некорректна: {total_text}"
  
