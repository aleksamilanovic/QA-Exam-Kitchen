import pytest
from pytest_bdd import when, then, scenarios
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

scenarios("../features/organize.feature")

expected_celebrant = "Aleksa Mianovic"
expected_organizer = "Aleksa"
expected_age = "27"
expected_date = "2023-02-05"
expected_time = "14:45"
expected_guests = "2-5"
expected_alergies = "Yes"
celebrant_value, organizer_value, age_value, date_value, time_value, guests_value, alergies_value = "", "", "", "", "", "", ""


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get("http://10.15.1.204:3000/reserve")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@when("We fill every field with valid data")
def test_organize(browser):
    organizer_field = browser.find_element(By.XPATH, "(//input[@type='text'])[1]")
    organizer_field.send_keys("Aleksa")
    birthdayperson_field = browser.find_element(By.XPATH, "(//input[@type='text'])[2]")
    birthdayperson_field.send_keys("Aleksa Milanovic")
    age_field = browser.find_element(By.XPATH, "//input[@type='number']")
    age_field.send_keys("27")
    date_field = browser.find_element(By.XPATH, "//input[@type='date']")
    date_field.send_keys("252023")
    time_field = browser.find_element(By.XPATH, "//input[@type='time']")
    time_field.send_keys("0245PM")
    people_field = browser.find_element(By.XPATH, "//select[@id='persons']/option[text()='2-5']")
    people_field.click()
    alergies_fields = browser.find_element(By.XPATH, "(//input[@type='radio'])[1]")
    alergies_fields.click()
    which_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@type='checkbox'])[1]")))
    which_field.click()
    organize_button = browser.find_element(By.XPATH, '//a[@href="#ex1"]')
    organize_button.click()

    time.sleep(2)
    global celebrant_value, organizer_value, age_value, date_value, time_value, guests_value, alergies_value
    celebrant_value = browser.find_element(By.XPATH, "//span[text()='Aleksa Milanovic']")
    organizer_value = browser.find_element(By.XPATH, "//span[text()='Aleksa']")
    age_value = browser.find_element(By.XPATH, "//span[text()='27']")
    date_value = browser.find_element(By.XPATH, "//span[text()='2023-02-05']")
    time_value = browser.find_element(By.XPATH, "//span[text()='14:45']")
    guests_value = browser.find_element(By.XPATH, "//span[text()='2-5']")
    alergies_value = browser.find_element(By.XPATH, "//span[text()='Yes']")


@then("Data in local storage is filled properly")
def test_organize():
    assert (celebrant_value, expected_celebrant)
    assert (organizer_value, expected_organizer)
    assert (age_value, expected_age)
    assert (time_value, expected_time)
    assert (time_value, expected_time)
    assert (guests_value, expected_guests)
    assert (alergies_value, expected_alergies)
