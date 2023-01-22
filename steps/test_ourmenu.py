import pytest
from pytest_bdd import when, then, scenarios
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

scenarios("../features/ourmenu.feature")


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get("http://10.15.1.204:3000/menu")
    driver.maximize_window()
    driver.execute_script("window.scrollTo(0, 900);")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@when("We choose the products by clicking on the plus button")
def test_ourmenudata(browser):
    buttons = browser.find_elements(By.XPATH, "//button[@class='btn btn-primary btnPlus']")
    selected_buttons = random.sample(buttons, 6)
    global expected_price, price
    expected_price = ""
    for button in selected_buttons:
        time.sleep(7)
        button.click()
        time.sleep(2)
        price_element = browser.find_element(By.XPATH, "//span[@id='ukupno']")
        price = price_element.text
        expected_price += price


@then("We get a valid price in ourmenu")
def test_ourmenudata():
    assert (expected_price, price)
