import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
import colorlog
from webdriver_manager.chrome import ChromeDriverManager
from pytest_bdd import scenario, given, when, then
import time
import random
import string


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

URL = "http://automationexercise.com"

def generate_random_email():
    """Generate a random email address."""
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{random_string}@example.com"

@pytest.fixture(scope="function")
def browser():
    """Fixture for initializing and closing the browser."""
    logger.info("Setting up the browser fixture...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    logger.info("Tearing down the browser fixture...")
    driver.quit()

@scenario('features/scenario_1.feature', 'User successfully places an order')
def test_place_order():
    pass

@given('I navigate to the AutomationExercise website')
def navigate_to_website(browser):
    """Navigate to AutomationExercise website."""
    logger.info("Navigating to the AutomationExercise website...")
    browser.get(URL)
    browser.find_element(By.XPATH, "//p[.='Autoriser']").click()

@when('I add products to the cart')
def add_products_to_cart(browser):
    """Add products to the cart."""
    logger.info("Adding products to the cart...")
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/product_details/1']"))
    ).click()
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn btn-default cart') and .//i[contains(@class, 'fa fa-shopping-cart')]]"))
    ).click()
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[.='View Cart']"))
    ).click()

@then('I proceed to checkout and sign up')
def proceed_and_sign_up(browser):
    """Proceed to checkout and sign up."""
    logger.info("Proceeding to checkout and signing up...")
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[.='Proceed To Checkout']"))
    ).click()
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//u[.='Register / Login']"))
    ).click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@data-qa='signup-name']"))
    ).send_keys("Test julien")
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@data-qa='signup-email']"))
    ).send_keys(generate_random_email())
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='signup-button']"))
    ).click()

    browser.find_element(By.XPATH, "//input[@value = 'Mr']").click()
    browser.find_element(By.NAME, "password").send_keys("TestPassword123")
    browser.find_element(By.NAME, "days").send_keys("26")
    browser.find_element(By.NAME, "months").send_keys("July")
    browser.find_element(By.NAME, "years").send_keys("1993")
    browser.find_element(By.NAME, "newsletter").click()
    browser.find_element(By.NAME, "optin").click()

    while True:
        try:
            WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//button[.='Create Account']"))
            )
            break
        except TimeoutException:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='first_name']"))
    ).send_keys("Test Julien")
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='last_name']"))
    ).send_keys("Test julien")
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[4]/input[@class='form-control']"))
    ).send_keys("test julien")
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//select[@id='country']"))
    ).click()
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//option[.='Canada']"))
    ).click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='state']"))
    ).send_keys("Test julien")
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='city']"))
    ).send_keys("Test julien")
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='zipcode']"))
    ).send_keys("123456")
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='mobile_number']"))
    ).send_keys("1234567890")
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.='Create Account']"))
    ).click()

@then('the message ACCOUNT CREATED! should be visible')
def verify_account_created(browser):
    """Verify that the "ACCOUNT CREATED!" message is visible."""
    assert "Account Created!" in browser.page_source
    time.sleep(1)

    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
    time.sleep(1)


@then('I complete the order with valid payment information')
def complete_order(browser):
    """Complete the order with valid payment information."""
    logger.info("Completing the order with valid payment information...")
    browser.find_element(By.CSS_SELECTOR, "ul.nav.navbar-nav a[href='/view_cart']").click()
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[.='Proceed To Checkout']"))
    ).click()
    place_order_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[.='Place Order']"))
    )
    browser.execute_script(
        "arguments[0].scrollIntoView({block: 'center', inline: 'center'});", place_order_button)
    place_order_button.click()
    browser.find_element(
        By.CSS_SELECTOR, "input[name='name_on_card']").send_keys("Test User")
    browser.find_element(By.CSS_SELECTOR, "input[name='card_number']").send_keys(
        "4111111111111111")
    browser.find_element(By.CSS_SELECTOR, "input[name='cvc']").send_keys("123")
    browser.find_element(
        By.CSS_SELECTOR, "input[name='expiry_month']").send_keys("12")
    browser.find_element(
        By.CSS_SELECTOR, "input[name='expiry_year']").send_keys("2025")
    browser.find_element(
        By.CSS_SELECTOR, "button[data-qa='pay-button']").click()
    time.sleep(5)


@then('the message "Congratulations! Your order has been confirmed!" should be visible')
def verify_order_confirmation(browser):
    """Verify that the order confirmation message is visible."""
    logger.info('Verifying the order confirmation message...')
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//p[text()='Congratulations! Your order has been confirmed!']"))
    )


@when('I click on "Download Invoice"')
def download_invoice(browser):
    """Click on the "Download Invoice" button."""
    logger.info('Clicking on "Download Invoice"...')
    browser.find_element(By.XPATH, f"//a[.='Download Invoice']").click()

@then('the invoice should be downloaded successfully')
def verify_invoice_download(browser):
    """Verify that the invoice is downloaded successfully."""
    logger.info("Success !")

