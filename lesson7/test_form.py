    form_page.complete_the_form()
    form_page.sublime_click()
    form_page.zip_code_red()
    form_page.other_green()

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
    
    # Закрытие браузера
    driver.quit()
