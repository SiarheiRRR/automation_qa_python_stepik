import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


def filling_pages(url):
    with webdriver.Chrome() as browser:
        browser.get(url)
        browser.implicitly_wait(1)
        browser.find_element(By.XPATH, '//label[text()="First name*"]/following-sibling::input').send_keys('first_name')
        browser.find_element(By.XPATH, '//label[text()="Last name*"]/following-sibling::input').send_keys('last_name')
        browser.find_element(By.XPATH, '//label[text()="Email*"]/following-sibling::input').send_keys('email')
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        return browser.find_element(By.TAG_NAME, "h1").text

class TestPages(unittest.TestCase):
    def test_register_url1_registration(self):
        testing_url = 'http://suninjuly.github.io/registration1.html'
        self.assertEqual(filling_pages(testing_url), 'Congratulations! You have successfully registered!',
                         'welcome text is not correct!')

    def test_register_url2_registration(self):
        testing_url = 'http://suninjuly.github.io/registration2.html'
        self.assertEqual(filling_pages(testing_url), 'Congratulations! You have successfully registered!',
                         'welcome text is not correct!')


if __name__ == "__main__":
    unittest.main()