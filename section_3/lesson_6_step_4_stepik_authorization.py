# import pytest
# from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os
class TestLogin:
    @staticmethod
    def test_guest_should_see_login_link(browser):
        link = f"https://stepik.org/lesson/236895/step/1"
        login = os.getenv('STEPIK_USER')
        password = os.getenv('STEPIK_PASSWORD')
        browser.get(link)
        browser.implicitly_wait(5)
        browser.find_element(By.ID, "ember33").click()
        browser.find_element(By.ID, "id_login_email").send_keys(login)
        browser.find_element(By.ID, "id_login_password").send_keys(password)
        browser.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader').click()
        sleep(5)
