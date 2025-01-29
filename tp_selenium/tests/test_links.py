import pytest
import time
import requests
import logging
import colorlog
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from pytest_bdd import scenario, given, when, then

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

### _________________________________________________________####

# Séparation pour les logs
SEPARATOR = "----------------------------------------"


# 🎯 URL of the test page
URL_links = "https://demoqa.com/links"


@pytest.fixture(scope="function")
def browser():
    """Fixture pour le navigateur Selenium."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# 📌 Cucumber scenario binding


@scenario("features/links.feature", "Check response status for all API call links")
def test_links():
    pass


@given("the user is on the DemoQA links page")
def open_demoqa_links_page(browser):
    """Navigate to the DemoQA Links page."""
    logger.info(f"Navigating to the DemoQA links page: {URL_links}")
    logger.debug(SEPARATOR)
    browser.get(URL_links)
    

@when("they click on each link in the API call section")
def click_api_links(browser):
    """Click each API call link and assert the expected response."""
    links = {
        "created": ("201", "Created"),
        "no-content": ("204", "No Content"),
        "moved": ("301", "Moved Permanently"),
        "bad-request": ("400", "Bad Request"),
        "unauthorized": ("401", "Unauthorized"),
        "forbidden": ("403", "Forbidden"),
        "invalid-url": ("404", "Not Found"),
    }

    for link_id, (status_code, status_text) in links.items():
        logger.info(SEPARATOR)
        logger.info(f"Attempting to click the link with ID: {link_id}")
        logger.debug(SEPARATOR)

        try:
            # Find the link element and scroll into view
            link = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//a[@id = '{link_id}']"))
            )
            logger.info(SEPARATOR)
            logger.info(f"Found the link with ID: {
                        link_id}. Scrolling into view.")
            browser.execute_script(
                "arguments[0].scrollIntoView({block: 'center', inline: 'center'});", link)

            # Wait until the link is clickable
            link = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//a[@id = '{link_id}']"))
            )
            logger.info(SEPARATOR)
            logger.info(f"Clicking on the link with ID: {link_id}.")
            link.click()

            # Wait for the link response to appear
            link_response = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//p[@id = 'linkResponse']"))
            )
            logger.info(SEPARATOR)
            logger.info(f"Response for link with ID: {
                        link_id} has appeared. Verifying it...")

            # Expected response message
            expected_response = f"Link has responded with staus {
                status_code} and status text {status_text}"
            actual_response = link_response.text.strip()

            # Log the actual and expected responses
            logger.debug(f"Expected response: {expected_response}")
            logger.debug(f"Actual response: {actual_response}")

            # Assert that the expected response is part of the actual response
            assert expected_response in actual_response, \
                f"Expected '{expected_response}', but got '{actual_response}'"

            logger.info(f"Link with ID: {
                        link_id} has responded correctly with status {status_code}.")

        except TimeoutException as e:
            logger.error(f"Timeout occurred for link with ID: {
                         link_id}. Error: {str(e)}")
            raise

        except Exception as e:
            logger.error(f"An error occurred while handling the link with ID: {
                         link_id}. Error: {str(e)}")
            raise


@then("they should receive a valid HTTP response code")
def validate_http_response(browser):
    """Vérifie que la réponse HTTP est valide pour chaque lien."""
    logger.info(SEPARATOR)
    logger.info("All links have been clicked and their responses validated.")
    logger.debug(SEPARATOR)

    # Wait before going to the next test
    logger.info(SEPARATOR)
    logger.info("Waiting 5 seconds before going to the next test.")
    time.sleep(5)
