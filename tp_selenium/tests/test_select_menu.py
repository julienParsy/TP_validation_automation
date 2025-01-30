import pytest
import logging
import colorlog
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    time.sleep(4)  
    browser.execute_script(
        "window.scrollTo({top: document.body.scrollHeight/2, behavior: 'smooth'})")

@when('they select Another Root option from the Select value dropdown')
def select_root_option(browser):
    logger.info("Clicking on the dropdown to expand it...")
    browser.execute_script("window.scrollTo({top: 500, behavior: 'smooth'})")
    dropdown = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "withOptGroup"))
    )
    dropdown.click()
    time.sleep(1)  
    logger.info("Dropdown expanded.")

@then('Another root option should be displayed')
def verify_another_root_option(browser):
    logger.info("Verifying 'Another root option' is visible...")
    option = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#fixedban div:nth-child(4)"))
    )
    assert option.is_displayed(), "Option 'Another root option' is not visible"


@scenario("features/select_menu.feature", "Select one > Another")
def test_select_one():
    print("Select one > Another")
    pass

@given("the user navigates to the select menu page")
def select_select_one(browser):
    print("Navigating to the select menu page...")
    browser.get(URL_SELECT_MENU)
    time.sleep(2)

@when('they select "Select One" dropdown')
def select_root_option(browser):
    print("Clicking on the dropdown to expand it...")
    logger.info("Clicking on the dropdown to expand it...")
    browser.execute_script("window.scrollTo({top: 500, behavior: 'smooth'})")
    dropdown = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "selectOne"))
    )
    dropdown.click()
    logger.info("Dropdown expanded.")
    time.sleep(1)  

@then('"Other" should be displayed')
def verify_another_root_option(browser):
    print("Verifying 'Other' is visible...")
    option = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@id = 'react-select-3-option-0-5']")
        )
    )
    option.click()
    time.sleep(1)  

    logger.info("Vérification de la visibilité de 'Other' dans l'élément avec ID 'selectOne'...")
    selected_option = browser.find_element(By.ID, "selectOne").text
    assert "Other" in selected_option, "'Other' n'est pas visible dans le dropdown 'selectOne'"
    logger.info("'Other' est correctement visible dans le dropdown 'selectOne'.")



@scenario("features/select_menu.feature", "Old Style menu > Aqua")
def test_old_style_menu():
    pass

@given("the user navigates to the select menu page")
def navigate_to_select_menu_page(browser):
    logger.info("Navigating to the select menu page...")
    browser.get(URL_SELECT_MENU)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "oldSelectMenu"))
    )
    logger.info("Page loaded successfully.")

@when('they select "Old Style" dropdown')
def select_root_option(browser):
    logger.info("Clicking on the dropdown to expand it...")
    browser.execute_script("window.scrollTo({top: 500, behavior: 'smooth'})")
    dropdown = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "oldSelectMenu"))
    )
    dropdown.click()
    time.sleep(1) 
    logger.info("Dropdown expanded.")

@then('"Aqua" should be displayed')
def verify_another_root_option(browser):
    logger.info("Verifying 'Aqua' is visible...")
    option = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#fixedban div:nth-child(4)"))
    )
    assert option.is_displayed(), "Option 'Aqua' is not visible"
    logger.info("Option 'Aqua' is visible.")




@scenario("features/select_menu.feature", "Drop down > all colors")
def test_drop_down():
    pass

@given("the user navigates to the select menu page")
def navigate_to_select_menu_page(browser):
    logger.info("Navigating to the select menu page...")
    browser.get(URL_SELECT_MENU)


    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "react-select-4-input"))
    )
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

@when('they select "Drop down" dropdown')
def select_all_colors(browser):
    logger.info("Clicking on the dropdown to expand it...")

    input_box = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "react-select-4-input"))
    )


    colors = ["Green", "Blue", "Black", "Red"]

    for color in colors:
        input_box.send_keys(color)  
        logger.info(f"Typing '{color}' in the dropdown...")


        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//div[contains(text(), '{color}')]"))
        )
        time.sleep(0.5)  
        input_box.send_keys(Keys.ENTER)  
        time.sleep(0.5)

    logger.info("✅ All colors have been selected.")

@then('all colors should be displayed')
def verify_all_colors_selected(browser):
    logger.info("Verifying all selected colors are visible...")


    selected_options = browser.find_elements(
        By.CSS_SELECTOR, ".css-1rhbuit-multiValue")
    selected_texts = [option.text for option in selected_options]

    expected_colors = ["Green", "Blue", "Black", "Red"]

    logger.info(f"Expected colors: {expected_colors}")
    logger.info(f"Actual selected colors: {selected_texts}")

    assert set(expected_colors) == set(
        selected_texts), "All colors were not selected!"
    logger.info("✅ All colors are correctly selected.")


# Test pour le "Standard Multi Select"
@scenario("features/select_menu.feature", "Multi select > Audi")
def test_multi_select_standard():
    pass


@given("the user navigates to the select menu page")
def navigate_to_select_menu_page(browser):
    logger.info("Navigating to the select menu page...")
    browser.get(URL_SELECT_MENU)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "select"))
    )
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")


@when('they select "Multi select" dropdown')
def select_audi_standard(browser):
    logger.info("Selecting 'Audi' in the Standard Multi Select dropdown...")

    multi_select = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "cars"))
    )

    select = Select(multi_select)
    select.select_by_visible_text("Audi")  # Sélectionne "Audi"

    logger.info("✅ 'Audi' has been selected.")


@then('"Audi" should be selected')
def verify_audi_selected_standard(browser):
    logger.info("Verifying 'Audi' is selected...")

    multi_select = browser.find_element(By.ID, "cars")
    select = Select(multi_select)

    selected_options = [option.text for option in select.all_selected_options]

    logger.info(f"Selected options: {selected_options}")
    
    assert "Audi" in selected_options, "❌ 'Audi' was not selected!"
    logger.info("✅ 'Audi' is correctly selected.")


