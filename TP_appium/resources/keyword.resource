*** Settings ***
Documentation    Importe les libraries et les ressources
Library    String
Library    AppiumLibrary

Resource    ../resources/variable.resource
Resource    ../resources/library.resource


*** Keywords ***
Open Application To API Demos
    [Documentation]    Test pour ouvrir l'application API Demos
    Open Application
    ...    ${REMOTE_URL}
    ...    platformName=${PLATFORM_NAME}
    ...    platformVersion=${PLATFORM_VERSION}
    ...    deviceName=${DEVICE_NAME}
    ...    appActivity=${API_DEMOS_APP_ACTIVITY}
    ...    appPackage=${API_DEMOS_APP_PACKAGE}

    Page Should Contain Element    id=android:id/list

I Open Views
    [Documentation]    Cliquer sur Views dans le menu principal.
    Click Element If Visible    ${VIEWS}

I Open Animation Page And I Click On Push Button
    [Documentation]    Cliquer sur Animation dans le menu principal.
    Click Element If Visible   ${ANIMATION_BUTTON}
    Click Element If Visible   ${PUSH_BUTTON}

I Select Hyperspace Animation And I Check Message
    [Documentation]    Cliquer sur Hyperspace dans le menu principal.
    Click Element If Visible   ${SELECT_ANIMATION}
    Click Element If Visible   ${HYPERSPACE}
    Wait Until Element Is Visible    //android.widget.TextView[@content-desc="Freedom"]    timeout=20s
    ${part1}=    Get Text    //android.widget.TextView[@content-desc="Freedom"]
    Wait Until Element Is Visible    //android.widget.TextView[@content-desc="is nothing else but"]    timeout=20s
    ${part2}=    Get Text    //android.widget.TextView[@content-desc="is nothing else but"]
    Wait Until Element Is Visible    //android.widget.TextView[@content-desc="a chance to be better."]    timeout=20s
    ${part3}=    Get Text    //android.widget.TextView[@content-desc="a chance to be better."]
    Wait Until Element Is Visible    //android.widget.TextView[@content-desc="— Albert Camus"]    timeout=20s
    ${part4}=    Get Text    //android.widget.TextView[@content-desc="— Albert Camus"]
    ${full_text}=    Set Variable    ${part1} ${part2} ${part3} ${part4}
    Log    The full text is : ${full_text}

I Open Chronometer Page And I Click On Start Button
    [Documentation]    Cliquer sur Chronometer dans le menu principal.
    Click Element If Visible   ${CHRONOMETER}
    Click Element If Visible   ${START_BUTTON}
    ${time}=    Get Text    io.appium.android.apis:id/chronometer
    Log     : ${time}
    Click Element If Visible   ${FORMAT_BUTTON}
    Wait Until Element Is Visible    io.appium.android.apis:id/chronometer    timeout=20s
    ${formatted_time}=    Get Text    io.appium.android.apis:id/chronometer
    Log     : ${formatted_time}

I Open Seekbar And I Put To 88
    [Documentation]    Cliquer sur Seekbar dans le menu principal.
    Swipe    500    1500    200    500    800
    Swipe    500    1500    200    500    800
    Swipe    500    1500    200    500    800
    Click Element If Visible    ${seekbar_button}
    Click Element If Visible    ${SEEKBAR}
    Swipe    ${908}    ${309}    ${917}    ${309}
    Get Text    ${PROGRESS}
    Should Contain    ${PROGRESS}    88 from touch=true
