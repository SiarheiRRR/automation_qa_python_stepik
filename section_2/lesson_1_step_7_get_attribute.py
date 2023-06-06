from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from time import sleep

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/get_attribute.html')
    trs = int(browser.find_element(By.ID, 'treasure').get_attribute('valuex'))
    result = calc(trs)
    browser.find_element(By.ID, 'answer').send_keys(result)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()

