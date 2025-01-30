import pytest
import time
import logging
import colorlog
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

# Configuration des tests
URL_TOOLTIP = "https://demoqa.com/tool-tips"


@pytest.fixture(scope="function")
def browser():
    """Initialise le navigateur Selenium."""
    logger.info("Initializing the Chrome browser...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.execute_script("document.body.style.zoom='10%'")
    driver.implicitly_wait(10)
    yield driver
    logger.info("Closing the browser.")
    driver.quit()

# Définition du scénario BDD


@scenario("features/tooltip.feature", "Verify tooltip appears on hover")
def test_tooltip():
    """Test de l'affichage du tooltip sur hover."""
    pass


@given("the user navigates to the page containing the tooltip")
def navigate_to_tooltip_page(browser):
    """Navigue vers la page contenant le tooltip."""
    logger.info("Navigating to the tooltip test page...")
    try:
        browser.get(URL_TOOLTIP)
        time.sleep(2)
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "toolTipButton"))
        )
        logger.info("Page loaded successfully.")
    except Exception as e:
        logger.error(f"Failed to navigate to the tooltip page: {e}")
        raise


@when("they hover over the Tooltip element")
def hover_over_tooltip_element(browser):
    """Survole chaque élément pour afficher son tooltip, puis réinitialise l'état du curseur."""
    logger.info("Scrolling to the tooltip elements...")
    browser.execute_script("window.scrollTo(0, 500)")

    elements = [
        (By.ID, "toolTipButton"),
        (By.ID, "toolTipTextField"),
        (By.LINK_TEXT, "Contrary"),
        (By.LINK_TEXT, "1.10.32")
    ]

    for locator in elements:
        try:
            element = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located(locator)
            )
            # Survole l'élément
            actions = ActionChains(browser)
            actions.move_to_element(element).perform()
            logger.debug(f"Hovering over element with locator: {locator}.")
            # Attend que le tooltip apparaisse
            WebDriverWait(browser, 5).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "tooltip-inner"))
            )
            logger.info(
                f"Tooltip displayed for element with locator: {locator}.")
            # Déplace le curseur vers une zone neutre pour fermer le tooltip
            actions.move_to_element_with_offset(
                browser.find_element(By.TAG_NAME, 'body'), 0, 0
            ).perform()
            logger.debug("Moved cursor to neutral area to close the tooltip.")
        except Exception as e:
            logger.error(f"Failed to hover over element with locator {
                         locator}: {e}")
            raise

    logger.info("Completed hovering over all tooltip elements.")


@then("the tooltip should appear with the associated text")
def verify_tooltip_appearance(browser):
    """Vérifie que chaque tooltip apparaît avec le texte associé après le survol de l'élément."""
    elements_with_tooltips = {
        "toolTipButton": "You hovered over the Button",
        "toolTipTextField": "You hovered over the text field",
        "Contrary": "You hovered over the Contrary",
        "1.10.32": "You hovered over the 1.10.32"
    }

    for element_id, expected_tooltip_text in elements_with_tooltips.items():
        try:
            if element_id in ["Contrary", "1.10.32"]:
                element_locator = (By.LINK_TEXT, element_id)
            else:
                element_locator = (By.ID, element_id)

            # Déplace le curseur vers une zone neutre avant chaque survol
            actions = ActionChains(browser)
            actions.move_to_element_with_offset(
                browser.find_element(By.TAG_NAME, 'body'), 0, 0
            ).perform()
            logger.debug("Moved cursor to neutral area before hovering.")

            element_to_hover = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located(element_locator)
            )
            # Survole l'élément
            actions.move_to_element(element_to_hover).perform()
            logger.debug(f"Hovering over element '{element_id}'.")

            # Attend que le tooltip apparaisse
            WebDriverWait(browser, 5).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "tooltip-inner"))
            )

            # Vérifie le texte du tooltip
            tooltip = browser.find_element(By.CLASS_NAME, "tooltip-inner")
            assert tooltip.text == expected_tooltip_text, (
                f"Tooltip text for '{
                    element_id}' did not match expected text. "
                f"Expected: '{expected_tooltip_text}', but got: '{
                    tooltip.text}'"
            )
            logger.info(f"Verified tooltip for '{
                        element_id}': '{tooltip.text}'.")

            # Réinitialise les actions
            actions.move_to_element_with_offset(
                browser.find_element(By.TAG_NAME, 'body'), 0, 0
            ).perform()
            logger.debug("Moved cursor to neutral area after verification.")

        except Exception as e:
            logger.error(f"Failed to verify tooltip for '{element_id}': {e}")
            raise

    logger.info("All tooltips verified successfully.")
