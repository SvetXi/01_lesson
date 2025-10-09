from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 3) Дождаться картинки (loading images)
driver = webdriver.Firefox()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Дождаться загрузки всех картинок – проверим, что у всех картинок атрибут complete True через JS
WebDriverWait(driver, 10).until(
    lambda d: d.execute_script("return Array.from(document.images).every(img => img.complete);")
)

# Получить src 3-й картинки (индексация с 0)
third_img_src = driver.find_elements(By.TAG_NAME, "img")[2].get_attribute("src")
print(third_img_src)

driver.quit()
