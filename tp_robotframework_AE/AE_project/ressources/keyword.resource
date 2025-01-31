*** Settings ***
Documentation    This is the documentation for the suite.
Resource    ../ressources/variables.resource
Resource    ../ressources/library.resource


*** Keywords ***
# Feature: Product Search
# @SimpleSearch
# Scenario: Search for a specific product and verify the results


The User Navigates To Website
    [Documentation]    Navigating to the website
    Log    Ouvrir le navigateur avec l'url ${url} et le browser ${browser}
    Open Browser    ${url}    ${browser}
    Log    Maximiser la taille de la fenêtre
    Maximize Browser Window
    Log    Supprimer les cookies
    Click Element If Visible    ${accept_cookies}
    Log    Vérifier si le logo est visible
    Wait Until Element Is Visible    ${logo}    timeout=10
    Log    La page d'accueil est visible

The User Clicks On The Products Button
    [Documentation]    Clicking on the "Products" button
    Log    Cliquer sur le bouton "Products"
    Click Element If Visible    ${products_button}
    Log    Bouton "Products" cliqué

The User Is Successfully Redirected To The "ALL PRODUCTS" Page
    [Documentation]    Verifying we are on the "ALL PRODUCTS" page
    Wait Until Element Is Visible    ${all_products_heading_text}    timeout=10
    Log    Le texte de l'en-tête "ALL PRODUCTS" est visible
    ${heading_text}=    Get Text    ${all_products_heading_text}
    Should Be Equal    ${heading_text}    ALL PRODUCTS
    Log    ${heading_text}
    Log    La page "ALL PRODUCTS" est visible

The User Enters "${products}" In The Search Bar And Clicks The "Search" Button
    [Documentation]    Entering "${products}" in the search bar and clicking the "Search" button
    Log    Entrer "${products}" dans la barre de recherche
    Enter Text    ${search_box}    ${products}
    Log    Texte "${products}" entré dans la barre de recherche
    Log    Cliquer sur le bouton "Search"
    Click Element If Visible    ${search_button}
    Log    Bouton "Search" cliqué

The Searched "${products}" Are Visible
    [Documentation]    Verifying the searched "${products}" are visible
    Log    La recherche de "${products}" est visible
    Wait Until Element Is Visible    ${all_products_heading_text}    timeout=10
    Wait Until Element Is Visible    ${product_overlay}    timeout=10
    Log    L'overlay du produit est visible
    Scroll Element Into View    ${product_overlay}
    ${item}=    Get WebElements    ${product_overlay}
    ${products_count}=    Get Length    ${item}
    Log    Nombre de produits trouvés: ${products_count}
    Should Be True    ${products_count} > 0
    Log    Les produits recherchés sont visibles

The Displayed Results Contain "${products}"
    [Documentation]    Verifying the displayed results contain "${products}"
    Log    Vérification que les résultats affichés contiennent "${products}"
    Wait Until Element Is Visible    ${PRODUCT_CARDS}    timeout=5s
    ${product_text}=    Get Text    ${item_title}
    Log    Texte du produit: ${product_text}
    Should Contain    ${product_text}    ${products}
    Log    Les résultats affichés contiennent "${products}"

# Feature: User Registration, Shopping, and Account Deletion
# @vérifier les détails de l'adresse sur la page de paiement
#   Scenario: Register, Shop, Checkout, and Delete Account

When The User Clicks On The "Signup/Login" Button
    [Documentation]    Clicking on the "Signup/Login" button
    Log    Cliquer sur le bouton "Signup/Login"
    Click Element If Visible    ${signup_login_button}
    Log    Bouton "Signup/Login" cliqué

The User Fills In All The Registration Details And Creates An Account
    [Documentation]    Filling in all the registration details and creating an account
    Log    Remplir tous les champs de registration
    Click Element If Visible    ${signup_login_button}
    Log    Bouton "Signup/Login" cliquée
    Click Element If Visible    ${signup_button}
    Enter Text    ${NAME_INPUT}    Julien
    Fill Email Field With Random Email    ${EMAIL_INPUT}

The Message "ACCOUNT CREATED!" Should Be Displayed
    [Documentation]    Verifying the message "ACCOUNT CREATED!" is displayed
    Log    Vérifier si le message "ACCOUNT CREATED!" est affiché

#     Wait Until Element Is Visible    ${account_created_message}    timeout=10
#     Log    Message "ACCOUNT CREATED!" affiché
#     ${message}=    Get Text    ${account_created_message}
#     Should Be Equal    ${message}    ACCOUNT CREATED!
#     Log    ${message}
#     Click Element If Visible    css:button[data-qa='signup-button']
#     Click Element If Visible    xpath://input[@value = 'Mr']
#     Enter Text    name:password    TestPassword123
#     Enter Text    name:days    26
#     Enter Text    name:months    July
#     Enter Text    name:years    1993
#     Click Element If Visible    name:newsletter
#     Click Element If Visible    name:optin
#     And the user clicks on the "Continue" button
#     Then the message "Logged in as username" should be visible at the top

#     When the user adds products to the cart
#     And the user clicks on the "Cart" button
#     Then the cart page should be displayed

#     When the user clicks on "Proceed to Checkout"
#     Then the delivery address should match the registered address
#     And the billing address should match the registered address

#     When the user clicks on the "Delete Account" button
#     Then the message "ACCOUNT DELETED!" should be displayed
#     And the user clicks on the "Continue" button
