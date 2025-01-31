*** Settings ***
Documentation    This is the documentation for the suite.
Library    String
Library    SeleniumLibrary
Library    FakerLibrary


*** Keywords ***
Click Element If Visible
    [Documentation]    This keyword clicks an element
    [Arguments]    ${locator}
    Wait Until Element Is Visible    ${locator}    timeout=5s
    Log    Clicking on ${locator}
    Click Element    ${locator}

Enter Text
    [Documentation]    This keyword fills a text field
    [Arguments]    ${locator}    ${value}
    Input Text    ${locator}    ${value}

Generate Random Email
    ${random_number}=    Evaluate    random.randint(1000, 9999)    modules=random
    ${email}=    Set Variable    user_${random_number}@$example.com
    Log    Email: ${email}

Fill Email Field With Random Email
    [Arguments]    ${locator}
    ${random_number}=    Evaluate    random.randint(1000, 9999)    modules=random
    ${random_email}=    Set Variable    user_${random_number}@example.com
    Enter Text    ${locator}    ${random_email}

