import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")
    yield driver
    driver.quit()


def test_checkbox_dynamic_behavior(driver):
    wait = WebDriverWait(driver, 10)

    remove_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkbox-example button")))
    remove_button.click()
    wait.until(EC.invisibility_of_element_located((By.ID, "checkbox")))
    
    add_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkbox-example button")))
    add_button.click()
    checkbox = wait.until(EC.presence_of_element_located((By.ID, "checkbox")))

    assert checkbox.is_displayed(), "Checkbox should be visible after adding."


def test_input_field_dynamic_behavior(driver):
    wait = WebDriverWait(driver, 10)

    enable_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example button")))
    enable_button.click()
    input_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example input")))

    assert input_field.is_enabled(), "Input field should be enabled."

    disable_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example button")))
    disable_button.click()
    wait.until(lambda d: not d.find_element(By.CSS_SELECTOR, "#input-example input").is_enabled())

    assert not driver.find_element(By.CSS_SELECTOR, "#input-example input").is_enabled(), \
        "Input field should be disabled."