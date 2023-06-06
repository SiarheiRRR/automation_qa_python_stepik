import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/file_input.html')
    tuple(inp.send_keys('test filled') for inp in browser.find_elements(By.CSS_SELECTOR, 'input.form-control'))
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '1.txt')           # добавляем к этому пути имя файла
    browser.find_element(By.ID, 'file').send_keys(file_path)
    sleep(1)
    browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    sleep(5)