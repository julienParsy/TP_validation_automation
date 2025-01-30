import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from pytest_bdd import scenario, given, when, then
import time
import logging
import colorlog
import os

### _________________Configuration du logger_________________###
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Formatter avec couleurs (optionnel)
formatter = colorlog.ColoredFormatter(
    "%(log_color)s[%(levelname)s] %(message)s",
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
)

# Ajout du handler pour afficher les logs
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

@pytest.fixture(scope="function")
def browser():
    """Fixture pour le navigateur Selenium."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@scenario('features/forms.feature', "Verify the presence of the contact form")
def test_input_field_presence():
    pass

@given('I am on the contact page')
def open_contact_page(browser):
    """Navigate to the contact form page."""
    logger.info("\n\nNavigating to the contact page.\n")
    browser.get('https://demoqa.com/automation-practice-form')

@when('I want to fill in the required fields')
def input_field_presence(browser):
    """Check the presence of required input fields."""
    fields = [
        'firstName', 'lastName', 'userEmail', 'userNumber',
        'dateOfBirthInput', 'uploadPicture', 'currentAddress',
        'state', 'city'
    ]

    checkboxes = [
        '//label[text()="Reading"]',
        '//label[text()="Music"]',
        '//label[text()="Sports"]'
    ]

    # Check if each field is visible on the page
    for field in fields:
        logger.debug(f"\n\nChecking presence of field: {field}\n")
        element = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, field))
        )
        assert element.is_displayed(), f"{field} is not displayed"

    # Check if checkboxes are visible
    for checkbox in checkboxes:
        logger.debug(f"\n\nChecking presence of checkbox: {checkbox}\n")
        element = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, checkbox))
        )
        assert element.is_displayed(), f"Checkbox for {checkbox} is not displayed"

@then('I should be able to fill in all fields')
def fill_input_fields(browser):
    """Fill in the required fields in the form."""
    logger.info("\n\nFilling in input fields.\n")
    # Define values for input fields
    firstname = "John"
    lastname = "Doe"
    userMail = "johndoe@example.com"
    gender = "Male"
    number_phone = "1234567890"
    address = "123 Main Street"

    # Fill text fields
    logger.debug("\n\nFilling text fields.\n")
    browser.find_element(By.ID, 'firstName').send_keys(firstname)
    assert browser.find_element(By.ID, 'firstName').get_attribute('value') == firstname, "Firstname not filled correctly"
    logger.info(f"\n\nFirstname filled with value: {firstname}\n")

    browser.find_element(By.ID, 'lastName').send_keys(lastname)
    assert browser.find_element(By.ID, 'lastName').get_attribute('value') == lastname, "Lastname not filled correctly"
    logger.info(f"\n\nLastname filled with value: {lastname}\n")

    browser.find_element(By.ID, 'userEmail').send_keys(userMail)
    assert browser.find_element(By.ID, 'userEmail').get_attribute('value') == userMail, "User email not filled correctly"
    logger.info(f"\n\nUser email filled with value: {userMail}\n")

    browser.find_element(By.XPATH, f'//label[text()="{gender}"]').click()

    browser.find_element(By.ID, 'userNumber').send_keys(number_phone)
    assert browser.find_element(By.ID, 'userNumber').get_attribute('value') == number_phone, "User number not filled correctly"
    logger.info(f"\n\nUser number filled with value: {number_phone}\n")

    # Scroll down to make the date picker visible
    browser.execute_script("window.scrollTo(0, 500);")

    # Select date of birth
    logger.debug("\n\nSelecting date of birth.\n")
    browser.find_element(By.ID, 'dateOfBirthInput').click()
    browser.find_element(By.CSS_SELECTOR, '.react-datepicker__month-select').click()
    browser.find_element(By.CSS_SELECTOR, "[value='1']").click()  # Month (January)
    browser.find_element(By.CSS_SELECTOR, '.react-datepicker__year-select').click()
    browser.find_element(By.CSS_SELECTOR, "[value='2023']").click()  # Year
    browser.find_element(By.CSS_SELECTOR, '.react-datepicker__day--001').click()  # Day 1

    # Scroll down to make checkboxes visible
    browser.execute_script("window.scrollTo(0, 500);")

    # Select checkboxes
    logger.debug("\n\nSelecting checkboxes.\n")
    browser.find_element(By.XPATH, '//label[text()="Reading"]').click()
    browser.find_element(By.XPATH, '//label[text()="Music"]').click()
    browser.find_element(By.XPATH, '//label[text()="Sports"]').click()

    # Fill subjects input
    logger.debug("\n\nFilling subjects input.\n")
    subjects_input = browser.find_element(By.XPATH, '//input[@id="subjectsInput"]')
    subjects_input.send_keys("Maths")
    subjects_input.send_keys("\n")

    # Fill address
    logger.debug("\n\nFilling address.\n")
    browser.execute_script("window.scrollTo(0, 500);")
    browser.find_element(By.ID, 'currentAddress').send_keys(address)

    # Select state and city
    logger.debug("\n\nSelecting state and city.\n")
    browser.find_element(By.ID, 'state').click()
    browser.find_element(By.XPATH, "//div[contains(text(),'NCR')]").click()
    browser.find_element(By.ID, 'city').click()
    browser.find_element(By.XPATH, "//div[contains(text(),'Delhi')]").click()

@then('I should be able to submit the form')
def submit_form(browser):
    """Submit the form and verify submission."""
    logger.info("\n\nSubmitting the form.\n")
    # Scroll down to the submit button
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Click the submit button
    logger.debug("\n\nClicking the submit button.\n")
    browser.find_element(By.ID, 'submit').click()

    # Wait for submission to complete
    logger.info("\n\nWaiting for submission to complete.\n")
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Thanks for submitting the form')]"))
    )
    logger.info("\n\nForm submitted successfully.\n")
    
    # Take a screenshot
    logger.info("\n\nTaking a screenshot.\n")
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )
    screenshot = element.screenshot_as_png
    screenshot_path = os.path.join(os.path.dirname(__file__), 'screenshots', 'form_submitted.png')
    with open(screenshot_path, 'wb') as f:
        f.write(screenshot)
    logger.info(f"\n\nScreenshot saved to {screenshot_path}\n")

    # Wait before going to the next test
    logger.info("\n\nWaiting 5 seconds before going to the next test.\n")
    time.sleep(5)

