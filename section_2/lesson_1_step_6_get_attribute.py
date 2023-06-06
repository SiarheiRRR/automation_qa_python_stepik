from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from time import sleep

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get('https://suninjuly.github.io/math.html')
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None, "Robots radio is selected by default"
    imTheRobotEl = browser.find_element(By.ID, 'robotCheckbox').get_attribute('required')
    print(imTheRobotEl)
