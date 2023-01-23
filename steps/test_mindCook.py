import pytest
from pytest_bdd import when, then, scenarios
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

value = 0
expected_value_first = "Avocado Benedict"
expected_value_second = "Strawberry Sundae"
expected_value_third = "Soy Salmon"
expected_value_fourth = "Culiflower Dipper"
expected_value_fifth = "Blonde"
actual_value = ""

scenarios("../features/mindcook.feature")


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get("http://10.15.1.204:3000/questionaire")
    driver.maximize_window()
    driver.execute_script("window.scrollTo(0, 500);")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@when("We choose the value by clicking on the plus button")
def test_mindcook(browser):
    global value, actual_value
    for i in range(1, 10):
        left_button = browser.find_element(By.XPATH, "(//div[@class='btn-group'])[{0}]/button[1]".format(i))
        right_button = browser.find_element(By.XPATH, "(//div[@class='btn-group'])[{0}]/button[2]".format(i))
        random_button = random.choice(["left", "right"])

        if random_button == "left":
            left_button.click()
            value += 1
        else:
            right_button.click()
            time.sleep(2)

    rmm_button = browser.find_element(By.XPATH, "//button[@id='readmymind']")
    rmm_button.click()
    time.sleep(2)
    actual_value = browser.find_element(By.XPATH, "//*[@id='recHeader']")


@then("We get a valid value")
def test_mindcook():
    if value in range(0, 2):
        assert (actual_value, expected_value_first)

    elif value in range(2, 4):
        assert (actual_value, expected_value_second)

    elif value in range(4, 6):
        assert (actual_value, expected_value_third)

    elif value in range(6, 8):
        assert (actual_value, expected_value_fourth)

    elif value in range(8, 10):
        assert (actual_value, expected_value_fifth)

    else:
        print("Error")
