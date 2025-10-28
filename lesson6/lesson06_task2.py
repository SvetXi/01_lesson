from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 2) Переименовать кнопку (text input)
driver = webdriver.Firefox()
driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")

button = driver.find_element(By.ID, "updatingButton")
button.click()

# Получить текст кнопки после нажатия
button_text = button.text
print(button_text)  # Ожидается: "SkyPro"

driver.quit()
