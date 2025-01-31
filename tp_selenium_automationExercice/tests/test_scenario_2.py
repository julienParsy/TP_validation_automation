import colorlog
import logging
import pytest
from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


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


@pytest.fixture(scope="function")
def browser():
    logger.info("Setting up the browser fixture...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    logger.info("Tearing down the browser fixture...")
    driver.quit()


@scenario('features/scenario_2.feature', 'User searches for a product, adds it to the cart, and manages the cart')
def test_search_and_manage_cart():
    pass


@given('the user navigates to "http://automationexercise.com"')
def open_homepage(browser):
    logger.debug("Navigating to %s", URL)
    browser.get(URL)
    try:
        allow_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//p[.='Autoriser']"))
        )
        allow_button.click()
        logger.info("Clicked 'Autoriser'")
    except Exception:
        logger.warning("'Autoriser' button not found or not needed.")


@when('the user clicks on the "Products" button')
def click_products(browser):
    logger.debug("Clicking on the 'Products' button")
    logger.info("Waiting for the 'Products' button to be clickable")
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/products']"))
    ).click()
    logger.info("Clicking on the 'Products' button")


@then('the user should be redirected to the "ALL PRODUCTS" page')
def verify_all_products_page(browser):
    logger.debug("Verifying we are on the 'ALL PRODUCTS' page")
    logger.info("Waiting for the 'ALL PRODUCTS' heading to be visible")
    all_products_heading = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[@class='title text-center']"))
    )
    assert all_products_heading.text == "ALL PRODUCTS"
    logger.info("Verified we are on the 'ALL PRODUCTS' page")


@when('the user searches for a product by entering a name in the search bar')
def enter_product_name(browser):
    logger.debug("Entering 'T-shirt' in the search bar")
    logger.info("Waiting for the search bar to be visible")
    search_box = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "search_product"))
    )
    search_box.send_keys("T-shirt")
    logger.info("Entering 'T-shirt' in the search bar")


@when('clicks the search button')
def click_search(browser):
    logger.debug("Clicking the search button")
    logger.info("Waiting for the search button to be clickable")
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id = 'submit_search']"))
    ).click()
    logger.info("Clicking the search button")


@then('the "SEARCHED PRODUCTS" section should be visible')
def verify_searched_products_section(browser):
    logger.debug("Verifying the 'SEARCHED PRODUCTS' section is visible")
    logger.info("Waiting for the 'SEARCHED PRODUCTS' heading to be visible")
    searched_products_heading = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[@class='title text-center']"))
    )
    assert searched_products_heading.text == "SEARCHED PRODUCTS"
    logger.info("Verified the 'SEARCHED PRODUCTS' section is visible")


@then('all matching products should be displayed')
def verify_matching_products(browser):
    logger.debug("Verifying all matching products are displayed")
    logger.info("Waiting for the first product to be visible")
    product_overlay = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "product-overlay"))
    )
    browser.execute_script("arguments[0].scrollIntoView(true);", product_overlay)
    products = browser.find_elements(By.CLASS_NAME, "product-overlay")
    assert len(products) > 0
    logger.info("Verified all matching products are displayed")


@when('the user adds all displayed products to the cart')
def add_products_to_cart(browser):
    logger.debug("Adding all displayed products to cart")
    products = browser.find_elements(By.CLASS_NAME, "product-image-wrapper")
    for product in products:
        logger.info("Adding a product to the cart")
        product.find_element(
            By.XPATH, ".//a[contains(@class, 'add-to-cart')]").click()
        logger.info("Waiting for the 'Continue Shopping' button to be clickable")
        WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[.='Continue Shopping']"))
        ).click()
        logger.info("Clicking the 'Continue Shopping' button")


@when('clicks on the "Cart" button')
def open_cart(browser):
    logger.debug("Opening the 'Cart' page")
    browser.execute_script("window.scrollTo(0, 0);")
    logger.info("Waiting for the 'Cart' button to be clickable")
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//ul[@class='nav navbar-nav']//a[contains(.,'Cart')]"))
    ).click()
    logger.info("Clicking the 'Cart' button")


@then('the added products should be visible in the cart')
def verify_cart_products(browser):
    logger.debug("Verifying the added products are visible in the cart")
    logger.info("Waiting for the first cart item to be visible")
    cart_items = browser.find_elements(By.CLASS_NAME, "cart_description")
    assert len(cart_items) > 0
    logger.info("Verified the added products are visible in the cart")


@when('the user clicks on "Signup / Login" and logs in successfully')
def login(browser):
    logger.debug("Logging in")
    logger.info("Waiting for the 'Proceed To Checkout' button to be clickable")
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[.='Proceed To Checkout']"))
    ).click()
    logger.info("Clicking the 'Proceed To Checkout' button")
    logger.info("Waiting for the 'Register / Login' button to be clickable")
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//u[.='Register / Login']"))
    ).click()
    logger.info("Clicking the 'Register / Login' button")

    logger.info("Waiting for the login email field to be visible")
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@data-qa='login-email']"))
    ).send_keys("julien@example.com")

    logger.info("Waiting for the login password field to be visible")
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@data-qa='login-password']"))
    ).send_keys("TestPassword123")

    logger.info("Waiting for the login button to be clickable")
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-qa='login-button']"))
    ).click()
    logger.info("Clicking the login button")
    logger.info("Waiting for the logout link to be visible")
    logout_link = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@href='/logout']"))
    )
    assert logout_link.is_displayed()
    logger.info("Verified the logout link is visible")
    logged_as = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(., 'Logged in as julien')]"))
    )
    assert logged_as.is_displayed()
    logger.info("Verified the logged in as message is visible")


@when('navigates back to the Cart page')
def navigate_back_to_cart(browser):
    logger.debug("Navigating back to the 'Cart' page")
    logger.info("Waiting for the 'Cart' button to be clickable")
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//ul[@class='nav navbar-nav']//a[contains(.,'Cart')]"))
    ).click()
    logger.info("Clicked the 'Cart' button")

@then('the previously added products should still be present')
def verify_products_persist(browser):
    logger.debug("Verifying the previously added products are still present")
    logger.info("Retrieving cart items")
    cart_items = browser.find_elements(By.CLASS_NAME, "cart_description")
    assert len(cart_items) > 0
    logger.info(f"Verified {len(cart_items)} products are still present in the cart")

@when('the user removes all products from the cart')
def remove_all_products(browser):
    logger.debug("Removing all products from the cart")
    logger.info("Retrieving all remove buttons")
    remove_buttons = browser.find_elements(
        By.CLASS_NAME, "cart_quantity_delete")
    for button in remove_buttons:
        logger.info("Clicking a remove button")
        button.click()
    logger.info("All products removed from the cart")

@then('the message "Cart is empty! Click here to buy products." should be displayed')
def verify_empty_cart_message(browser):
    logger.debug("Verifying the message 'Cart is empty!' is displayed")
    logger.info("Finding the empty cart message element")
    empty_cart_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//b[. ='Cart is empty!']")))
    assert "Cart is empty!" in empty_cart_message.text
    logger.info("Verified the empty cart message is displayed")

