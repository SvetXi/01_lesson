from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Lesson_07.form_01.pages.form_page import FormPage


def test_complete_the_form():
    # Инициализация драйвера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Создание экземпляра страницы
    form_page = FormPage(driver)

    # Выполнение тестовых действий
    form_page.complete_the_form()
    form_page.sublime_click()
    form_page.zip_code_red()

    # Закрытие браузера
    driver.quit()
