*** Settings ***
Library    random



*** Variables ***
#    BROWSER

${BROWSER}  chrome

#    URL

${URL}  https://automationexercise.com

${ACCEPT_COOKIES}  xpath=//p[.='Autoriser']
${LOGO}  xpath=//img[@alt='Website for automation practice']

#    DATA

${PRODUCTS}    Dress

#    Locator
${PRODUCTS_BUTTON}  xpath=//a[@href='/products']
${ALL_PRODUCTS_HEADING_TEXT}    xpath://h2[@class='title text-center']
${SEARCH_BOX}    id=search_product
${SEARCH_BUTTON}    xpath=//button[@id = 'submit_search']
${PRODUCT_OVERLAY}    class:product-overlay
${PRODUCT_CARDS}    //div[@class='productinfo text-center']//p
${ITEM_TITLE}    //div[@class='features_items']//div[@class='product-overlay']//p
${SIGNUP_LOGIN_BUTTON}    //a[contains(.,'Signup / Login')]
${SIGNUP_BUTTON}   //input[@data-qa='signup-name']
${NAME_INPUT}   //input[@data-qa='signup-name']
${EMAIL_INPUT}   //input[@data-qa='signup-email']
