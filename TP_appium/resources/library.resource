*** Settings ***
Documentation    Importe les libraries et les ressources
Library    Collections
Library    String
Library    AppiumLibrary

Resource   variable.resource


*** Keywords ***
Click Digit
    [Documentation]    Crée une fonction qui va convertir le chiffre en id et cliquer dessus
    [Arguments]    ${digit}
    ${locator}=    Set Variable    id=com.google.android.calculator:id/digit_${digit}
    Log    Clicking element 'id=com.google.android.calculator:id/digit_${digit}'.
    Click Element    ${locator}

Click Element If Visible
    [Documentation]    This keyword clicks an element
    [Arguments]    ${locator}
    Wait Until Element Is Visible    ${locator}    timeout=5s
    Page Should Contain Element    ${locator}
    Log    Clicking on ${locator}
    Click Element    ${locator}

Get Text From People Names List
    [Documentation]    Crée une fonction qui va chercher chaque élément, récupérer le texte et l'envoyer dans les logs
    [Arguments]    @{names}
    FOR    ${name}    IN    @{names}
        ${element}=    Get Text    //android.widget.TextView[@text="${name}"]
        Log    Element Text: ${element}
    END