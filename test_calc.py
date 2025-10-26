from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Lesson_07.calc_02.pages.CalcPage import CalcPage


def test_calculator():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    calc_page = CalcPage(driver)
    calc_page.delay()
    calc_page.calculator()
    calc_page.result()
    driver.quit()
