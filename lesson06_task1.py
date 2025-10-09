from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://uitestingplayground.com/ajax")

# Нажать на синюю кнопку
button = driver.find_element(By.ID, "ajaxButton")
button.click()

# Дождаться появления зеленой плашки с текстом
ajax_text = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
).text
print(ajax_text)  # Ожидается: "Data loaded with AJAX get request."

driver.quit()
