from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    # browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    # sleep(1)
    browser.find_element(By.CSS_SELECTOR, '.trollface.btn.btn-primary').click()
    sleep(1)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    val_x = int(browser.find_element(By.ID, 'input_value').text)
    result = calc(val_x)
    browser.find_element(By.ID, 'answer').send_keys(result)
    browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    sleep(5)