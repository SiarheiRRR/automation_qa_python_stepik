from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from time import sleep


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    val_x = int(browser.find_element(By.ID, 'input_value').text)
    result = calc(val_x)
    browser.find_element(By.ID, 'answer').send_keys(result)
    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    button.click()
    sleep(5)