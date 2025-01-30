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

# URL DemoQA
URL_DEMOQA = "https://demoqa.com/"

# Données utilisateur
DEMOQA_USER_PASSWORD = "Bb123456!"
DEMOQA_USERNAME = "Damation"
DEMOQA_FIRSTNAME = "Damien"
DEMOQA_LASTNAME = "Automation"

# Lancer le navigateur
@pytest.fixture(scope="function")
def browser():
    """Fixture pour le navigateur Selenium."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@scenario('features/bookstore.feature', 'Accès à l\'application Book Store')
def test_go_to_book_store(browser):
    """Accède à l'application Book Store"""
    pass


@given('I am on the Book Store application')
def test_register_to_book_store(browser):
    """S'enregistre à l'application Book Store"""
    browser.get(URL_DEMOQA + "register")

    # Remplir les champs d'enregistrement
    browser.find_element(
        By.XPATH, "//input[@id='firstname']").send_keys(DEMOQA_FIRSTNAME)
    browser.find_element(
        By.XPATH, "//input[@id='lastname']").send_keys(DEMOQA_LASTNAME)
    browser.find_element(
        By.XPATH, "//input[@id='userName']").send_keys(DEMOQA_USERNAME)
    browser.find_element(
        By.XPATH, "//input[@id='password']").send_keys(DEMOQA_USER_PASSWORD)

    # Captcha
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//iframe[contains(@src, 'recaptcha')]"))
    )
    browser.switch_to.frame(browser.find_element(
        By.XPATH, "//iframe[contains(@src, 'recaptcha')]"))
    browser.find_element(-
        By.XPATH, "//div[@class='recaptcha-checkbox-border']").click()
    browser.switch_to.default_content()

    # Valider l'enregistrement
    browser.find_element(By.XPATH, "//button[@id='register']").click()


@when('I register with a valid username and password')
def test_login_and_check_if_connected(browser):
    """Teste la connexion et vérifie si l'utilisateur est connecté"""
    browser.get(URL_DEMOQA + "login")

    # Connexion
    browser.find_element(
        By.XPATH, "//input[@id='userName']").send_keys(DEMOQA_USERNAME)
    browser.find_element(
        By.XPATH, "//input[@id='password']").send_keys(DEMOQA_USER_PASSWORD)
    browser.find_element(By.XPATH, "//button[@id='login']").click()

    # Vérifier si l'utilisateur est connecté
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//label[contains(.,'User Name :')]"))
    )
    user_name_label = browser.find_element(
        By.XPATH, "//label[@id='userName-value']").text
    assert DEMOQA_USERNAME in user_name_label, f"Expected username '{
        DEMOQA_USERNAME}', but got '{user_name_label}'"


@then('I should be able to login with my credentials')
def login_to_book_store(browser):
    pass

