*** Settings ***
Documentation    This is the documentation for the suite.
Resource    ../ressources/keyword.resource

Suite Teardown    Close All Browsers


*** Test Cases ***


Search for a specific product and verify the results
    [Documentation]    Search for a specific product and verify the results
    Given The User Navigates To Website
    When The User Clicks On The Products Button
    Then The User Is Successfully Redirected To The "ALL PRODUCTS" Page
    When The User Enters "Dress" In The Search Bar And Clicks The "Search" Button
    Then The Searched "Dress" Are Visible
    The Displayed Results Contain "Dress"

Register, Shop, Checkout, and Delete Account
    [Documentation]    Register, Shop, Checkout, and Delete Account
    Given The User Navigates To Website
    When The User Clicks On The "Signup/Login" Button
    Then The User Fills In All The Registration Details And Creates An Account
    Then The Message "ACCOUNT CREATED!" Should Be Displayed
    Sleep    5

    # When The User Clicks On The "Continue" Button
    # Then The Message "Logged In As Username" Should Be Visible At The Top
    # When The User Adds Products To The Cart
    # And The User Clicks On The "Cart" Button
    # Then The Cart Page Should Be Displayed
    # When The User Clicks On "Proceed To Checkout"
    # Then The Delivery Address Should Match The Registered Address
    # And The Billing Address Should Match The Registered Address
    # When The User Clicks On The "Delete Account" Button
    # Then The Message "ACCOUNT DELETED!" Should Be Displayed
    # And The User Clicks On The "Continue" Button
