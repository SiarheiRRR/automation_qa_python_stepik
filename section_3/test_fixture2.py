import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     return browser


# webrowser = pytest.fixture(lambda: webdriver.Chrome())

class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self):
        pytest.fixture(lambda: webdriver.Chrome()).get(link)
        pytest.fixture(lambda: webdriver.Chrome()).find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        pytest.fixture(lambda: webdriver.Chrome()).get(link)
        pytest.fixture(lambda: webdriver.Chrome()).find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")