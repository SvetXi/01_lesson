from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from Lesson_07.shop_03.pages.LoginPage import LoginPage
from Lesson_07.shop_03.pages.CartPage import CartPage
from Lesson_07.shop_03.pages.InformPage import InformPage
from Lesson_07.shop_03.pages.OverviewPage import OverviewPage


def test_shop():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    login_page = LoginPage(driver)
    login_page.login()
    cart_page = CartPage(driver)
    cart_page.cart()
    inform_page = InformPage(driver)
    inform_page.inform()
    overveiw_page = OverviewPage(driver)
    overveiw_page.overview()
    overveiw_page.assert_sum()
    driver.quit()
