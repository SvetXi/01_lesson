import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Lesson_07.calc_02.pages.CalcPage import CalcPage

@allure.feature("Тестирование калькулятора")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка вычисления с задержкой")
@allure.description("Тест проверяет, что калькулятор корректно вычисляет выражение с задержкой.")
def test_calculator():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    calc_page = CalcPage(driver)
    with allure.step("Установка задержки вычислений"):
        calc_page.delay()
    with allure.step("Выполнение вычисления 7 + 8"):
        calc_page.calculator()
    with allure.step("Проверка результата вычислений"):
        calc_page.result()
    driver.quit()
