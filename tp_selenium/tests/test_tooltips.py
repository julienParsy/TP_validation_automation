import pytest
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
import time
from selenium.common.exceptions import TimeoutException


### _________________ Configuration du logger _________________ ###
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


### _________________ Configuration des tests _________________ ###

# 🎯 URL de la page de test
URL_TOOLTIP = "https://demoqa.com/tool-tips"


@pytest.fixture(scope="function")
def browser():
    """Fixture pour gérer le navigateur Selenium."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# 📌 Définition du scénario BDD
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
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "toolTipButton"))
        )
        logger.info("Page loaded successfully.")
    except Exception as e:
        logger.error(f"Failed to navigate to the tooltip page: {e}")
        raise


@when("they hover over the Tooltip element")
def hover_over_tooltip_element(browser):
    """Vérifie le contenu du tooltip de chaque hover"""
    # Scroll vers le haut de la page pour que les tooltips soient visibles
    browser.execute_script("window.scrollTo(0, 500)")
    time.sleep(1)
    elements = [
        (By.XPATH, "//button[@id='toolTipButton']"),
        (By.XPATH, "//input[@id='toolTipTextField']"),
        (By.XPATH, "//a[text()='Contrary']"),
        (By.XPATH, "//a[text()='1.10.32']")
    ]

    for locator in elements:
        try:
            element = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located(locator)
            )
            actions = ActionChains(browser)
            actions.move_to_element(element).perform()
            WebDriverWait(browser, 5).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "tooltip-inner"))
            )
            logger.info(f"Hovered over element with locator: {locator}.")
        except Exception as e:
            logger.error(f"Failed to hover over element with locator {
                         locator}: {e}")
            raise

    logger.info("Completed hover actions for all elements.")
    time.sleep(1)



@then("the tooltip should appear with the associated text")
def verify_tooltip_appearance(browser):
    """Vérifie l'apparition des tooltips avec le texte associé après hover."""
    element_to_click = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[. = 'Tool Tips']"))
    )
    element_to_click.click()
    try:
        # Vérifie si la page est bien chargée
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "toolTipButton"))
        )

        # Vérification du contenu des tooltips
        elements_with_tooltips = {
            "toolTipButton": "You hovered over the Button",
            "toolTipTextField": "You hovered over the text field",
            "Contrary": "You hovered over the Contrary link",
            "1.10.32": "You hovered over the 1.10.32 link"
        }

        for element, tooltip_text in elements_with_tooltips.items():
            # Déterminer le type de localisation selon l'élément
            if element in ["Contrary", "1.10.32"]:
                element_locator = (By.LINK_TEXT, element)
            else:
                element_locator = (By.ID, element)

            # Attendre que l'élément soit visible et faire le hover
            element_to_hover = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located(element_locator)
            )
            ActionChains(browser).move_to_element(element_to_hover).perform()

            # Vérifier que le tooltip devient visible
            tooltip = WebDriverWait(browser, 5).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, ".tooltip-inner"))
            )
            assert tooltip.text == tooltip_text, (
                f"Tooltip text for {element} did not match expected text. "
                f"Expected: {tooltip_text}, but got: {tooltip.text}"
            )
            logger.info(f"Tooltip for element {element} displayed correctly.")

        logger.info("Page loaded and tooltips verified successfully.")

    except Exception as e:
        logger.error(
            f"Failed to navigate to the tooltip page or verify tooltips: {e}")
        raise
    finally:
        # Réinitialiser les actions après la vérification des tooltips
        # Réinitialise l'état des actions
        ActionChains(browser).release().perform()
        logger.info("Reset action chains after verification.")
