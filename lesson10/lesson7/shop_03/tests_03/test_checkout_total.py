import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Lesson7.shop_03.pages.LoginPage import LoginPage
from Lesson7.shop_03.pages.CartPage import CartPage
from Lesson7.shop_03.pages.InformPage import InformPage
from Lesson7.shop_03.pages.OverviewPage import OverviewPage

@allure.title("Сквозной тест покупки товара")
@allure.description("Тест проверяет полный сценарий покупки товара: авторизация, добавление в корзину, заполнение информации и проверка итоговой суммы.")
@allure.feature("Покупка товара")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    # Инициализация драйвера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Шаг 1: Авторизация на сайте
    with allure.step("Авторизация на сайте"):
        login_page = LoginPage(driver)
        login_page.login()

    # Шаг 2: Добавление товара в корзину
    with allure.step("Добавление товара в корзину"):
        cart_page = CartPage(driver)
        cart_page.cart()

    # Шаг 3: Заполнение информации о покупателе
    with allure.step("Заполнение информации о покупателе"):
        inform_page = InformPage(driver)
        inform_page.inform()

    # Шаг 4: Проверка итоговой суммы заказа
    with allure.step("Проверка итоговой суммы заказа"):
        overview_page = OverviewPage(driver)
        overview_page.overview()
        overview_page.assert_sum()

    # Закрытие драйвера
    driver.quit()
