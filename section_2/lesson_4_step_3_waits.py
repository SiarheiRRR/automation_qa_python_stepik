from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
import pyperclip

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    browser.find_element(By.ID, 'book').click()
    val_x = int(browser.find_element(By.ID, "input_value").text)
    result = calc(val_x)
    browser.find_element(By.ID, 'answer').send_keys(result)
    browser.find_element(By.ID, 'solve').click()
    alert = browser.switch_to.alert
    result_digit = alert.text.split(': ')[-1]
    print(result_digit)
    time.sleep(2)
    pyperclip.copy(result_digit)
    alert.accept()

