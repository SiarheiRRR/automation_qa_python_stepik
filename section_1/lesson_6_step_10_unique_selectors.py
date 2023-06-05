from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)
    #select required elements (first_name, last_name, email) and fill it:
    browser.find_element(By.XPATH, '//label[text()="First name*"]/following-sibling::input').send_keys('first_name')
    browser.find_element(By.XPATH, '//label[text()="Last name*"]/following-sibling::input').send_keys('last_name')
    browser.find_element(By.XPATH, '//label[text()="Email*"]/following-sibling::input').send_keys('email')
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    time.sleep(1)
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
