import pytest
import logging
import colorlog
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from pytest_bdd import scenario, given, when, then

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

URL_SELECT_MENU = "https://demoqa.com/select-menu"


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@scenario("features/select_menu.feature", "Select value another root option")
def test_select_value():
    pass


@given("the user navigates to the select menu page")
def navigate_to_select_menu_page(browser):
    logger.info("Navigating to the select menu page...")
    browser.get(URL_SELECT_MENU)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "withOptGroup"))
    )
    logger.info("Page loaded successfully.")


@when('they select Another Root option from the Select value dropdown')
def select_root_option(browser):
    logger.info("Clicking on the dropdown to expand it...")
    dropdown = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "withOptGroup"))
    )
    dropdown.click()
    time.sleep(1)  # Ensure the dropdown expands
    logger.info("Dropdown expanded.")


@then('Another root option should be displayed')
def verify_another_root_option(browser):
    logger.info("Verifying 'Another root option' is visible...")
    option = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#fixedban div:nth-child(4)"))
    )
    assert option.is_displayed(), "Option 'Another root option' is not visible"

# Add additional scenarios for "Select one", "Old Style menu", "Drop down", and "Multi select" following similar steps
