import pytest

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.edge.service import Service

from webdriver_manager.microsoft import EdgeChromiumDriverManager



def driver():

    # Автоматическое скачивание и установка драйвера Edge

    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    driver.maximize_window()

    yield driver

    driver.quit()



def test_form_submission(driver):

    # Открытие страницы

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")



    # Данные для заполнения формы

    form_data = {

        "firstName": "Иван",

        "lastName": "Петров",

        "address": "Ленина, 55-3",

        "email": "test@skypro.com",

        "phone": "+7985899998787",

        "zip": "",

        "city": "Москва",

        "country": "Россия",

        "jobPosition": "QA",

        "company": "SkyPro"

    }



    # Заполнение формы

    for field_name, value in form_data.items():

        driver.find_element(By.NAME, field_name).send_keys(value)



    # Нажимаем кнопку Submit

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()



    # Проверка, что поле Zip code подсвечено красным

    zip_code_field = driver.find_element(By.NAME, "zip")

    assert "error" in zip_code_field.get_attribute("class"), "Поле Zip code не подсвечено красным"



    # Проверка, что остальные поля подсвечены зеленым

    fields = driver.find_elements(By.CSS_SELECTOR, "input")

    for field in fields:

        if field != zip_code_field:

            assert "success" in field.get_attribute("class"), f"Поле {field.get_attribute('name')} не подсвечено зеленым"


