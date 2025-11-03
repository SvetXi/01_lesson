import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Lesson7.form_01.pages.form_page import FormPage

@allure.feature("Тестирование формы")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка заполнения формы и подсветки полей")
@allure.description("Тест проверяет корректность заполнения формы и подсветку полей.")
def test_complete_the_form():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    with allure.step("Заполнение формы данными"):
        form_page = FormPage(driver)
        form_page.complete_the_form()
    with allure.step("Нажатие кнопки 'Submit'"):
        form_page.sublime_click()
    with allure.step("Проверка подсветки поля 'Почтовый индекс' красным цветом"):
        form_page.zip_code_red()
    with allure.step("Проверка подсветки остальных полей зеленым цветом"):
        form_page.other_green()
    driver.quit()
