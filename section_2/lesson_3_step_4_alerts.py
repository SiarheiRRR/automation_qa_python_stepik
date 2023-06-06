from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/alert_accept.html')
    browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    confirm = browser.switch_to.alert
    confirm.accept()
    sleep(1)
    val_x = int(browser.find_element(By.ID, 'input_value').text)
    print(val_x)
    result = calc(val_x)
    browser.find_element(By.ID, 'answer').send_keys(result)
    browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    sleep(5)