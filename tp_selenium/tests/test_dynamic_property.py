import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import colorlog
from webdriver_manager.chrome import ChromeDriverManager
from pytest_bdd import scenario, given, when, then
import time


# Configuration du logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

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

handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

URL = "https://demoqa.com/dynamic-properties"


@pytest.fixture(scope="function")
def browser():
    """Fixture pour initialiser et fermer le navigateur."""
    logger.info("Setting up the browser fixture...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    logger.info("Tearing down the browser fixture...")
    driver.quit()


@scenario('features/dynamic_properties.feature', 'Test visibility of a button after delay')
def test_button_visibility():
    pass


@given('I navigate to the "Dynamic Properties" page')
def navigate_to_dynamic_properties(browser):
    """Navigate to the dynamic properties page."""
    logger.info("Navigating to the dynamic properties page...")
    browser.get(URL)


@when('I wait for 5 seconds')
def wait_for_button(browser):
    """Wait for 5 seconds to allow the button to appear."""
    logger.info("Waiting for 5 seconds...")
    time.sleep(5)


@then('the "Visible After 5 Seconds" button should be visible')
def verify_button_visibility(browser):
    """Verify that the button is visible."""
    logger.info("Verifying the button visibility...")
    button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'visibleAfter'))
    )
    assert button.is_displayed(), "Button is not displayed"


@scenario('features/dynamic_properties.feature', 'Test color change of a button')
def test_button_color_change():
    pass


@when('I wait for the color change')
def wait_for_color_change(browser):
    """Wait for the color change of the button."""
    logger.info("Waiting for the color change...")
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'colorChange'))
    )


@then('the button color should change')
def verify_button_color_change(browser):
    """Verify that the button color has changed."""
    logger.info("Verifying the button color change...")
    button = browser.find_element(By.ID, 'colorChange')
    initial_classes = button.get_attribute('class')
    WebDriverWait(browser, 10).until(
        lambda driver: 'mt-4 text-danger btn btn-primary' in button.get_attribute('class')
    )
    new_classes = button.get_attribute('class')
    assert initial_classes != new_classes, "Button color did not change"


@scenario('features/dynamic_properties.feature', 'Test disabled button')
def test_disabled_button():
    pass


@when('I wait for the "Button to be enabled"')
def wait_for_button_enablement(browser):
    """Wait for the "Button to be enabled" to be clickable."""
    logger.info("Waiting for the button to be enabled...")
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'enableAfter'))
    )


@then('the "Enable Button" should be clickable')
def verify_button_enabled(browser):
    """Verify that the button is clickable."""
    logger.info("Verifying the button is enabled...")
    button = browser.find_element(By.ID, 'enableAfter')
    assert button.is_enabled(), "Button is not enabled"

