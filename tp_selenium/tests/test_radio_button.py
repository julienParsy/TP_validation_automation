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

URL_RADIO_BUTTON = "https://demoqa.com/radio-button"

@scenario('features/radio_button.feature', "Click on all radio buttons and verify the messages")
def test_radio_buttons():
    """Scenario: Click on all radio buttons and verify the messages."""
    pass

@given('I am on the "Radio Button" page')
def open_radio_button_page(browser):
    """Naviguer vers la page des boutons radio."""
    logger.info("Navigating to the Radio Button page...")
    browser.get(URL_RADIO_BUTTON)

@when('I click on the "Yes" radio button')
def click_yes_button(browser):
    """Cliquer sur le bouton radio 'Yes'."""
    logger.info("Clicking on the 'Yes' radio button...")
    time.sleep(2)
    yes_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[. = 'Yes']"))
    )
    yes_button.click()

@then('I should see the message "Radio button Yes is checked"')
def verify_yes_message(browser):
    """Vérifier que le message correspondant au bouton 'Yes' s'affiche."""
    logger.info("Verifying the message for 'Yes' button...")
    message_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[@class='mt-3']"))
    )
    assert "You have selected Yes" in message_element.text, "Message for 'Yes' not found"

@then('I click on the "Impressive" radio button')
def click_impressive_button(browser):
    """Cliquer sur le bouton radio 'Impressive'."""
    logger.info("Clicking on the 'Impressive' radio button...")
    impressive_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[.='Impressive']"))
    )
    impressive_button.click()

@then('I should see the message "Radio button Impressive is checked"')
def verify_impressive_message(browser):
    """Vérifier que le message correspondant au bouton 'Impressive' s'affiche."""
    logger.info("Verifying the message for 'Impressive' button...")
    message_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[@class='mt-3']"))
    )
    assert "You have selected Impressive" in message_element.text, "Message for 'Impressive' not found"

@then('I verify that the "No" radio button is disabled')
def verify_no_button_disabled(browser):
    """Vérifier que le bouton radio 'No' est désactivé."""
    logger.info("Verifying the 'No' radio button is disabled...")
    no_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='noRadio']"))
    )
    assert not no_button.is_enabled(), "The 'No' radio button is not disabled"

