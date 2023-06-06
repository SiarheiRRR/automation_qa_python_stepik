from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/selects2.html')
    int_1 = int(browser.find_element(By.ID, 'num1').text)
    int_2 = int(browser.find_element(By.ID, 'num2').text)
    result = str(int_1+int_2)
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(result))
    # browser.find_element(By.ID, 'dropdown').click()
    # browser.find_element(By.CSS_SELECTOR, f"[value='{result}']").click()
    browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
    sleep(5)