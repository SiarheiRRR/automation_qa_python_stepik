from selenium import webdriver
from selenium.webdriver.common.by import By
import time
with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/huge_form.html')
    elements = browser.find_elements(By.TAG_NAME, 'input')
    for element in elements:
        element.send_keys('Answer')
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(30)