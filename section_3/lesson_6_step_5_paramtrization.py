import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import os
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestLogin:
    num_page = ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905']
    result = ''

    @classmethod
    @pytest.mark.parametrize('num_page', num_page)
    def test_guest_should_see_login_link(cls, browser, num_page):
        link = f"https://stepik.org/lesson/{num_page}/step/1"
        login = os.getenv('STEPIK_USER')
        password = os.getenv('STEPIK_PASSWORD')
        browser.get(link)
        browser.implicitly_wait(10)
        browser.find_element(By.ID, "ember33").click()
        browser.find_element(By.ID, "id_login_email").send_keys(login)
        browser.find_element(By.ID, "id_login_password").send_keys(password)
        browser.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader').click()
        try: #если есть кнопка "Solve again", жмем её
            browser.find_element(By.CSS_SELECTOR, ".again-btn.white").click()
        except NoSuchElementException:
            pass
        curr_time = str(math.log(int(time.time())))
        wait = WebDriverWait(browser, 10)
        enter_answer_window = wait.until((EC.element_to_be_clickable((
            By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea"))))
        enter_answer_window.send_keys(curr_time) #enter the answer
        browser.find_element(By.CSS_SELECTOR, 'button.submit-submission').click() #click to SUBMIT
        answer = browser.find_element(By.CSS_SELECTOR, 'p.smart-hints__hint').text
        if answer != 'Correct!':
            cls.result += answer
        print('result is: ', cls.result)
