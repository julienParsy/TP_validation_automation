*** Settings ***
Documentation    Importe les libraries et les ressources
Library    AppiumLibrary
Resource    ../resources/keyword.resource

Test Setup    Open Application To API Demos
Test Teardown    Close Application


*** Test Cases ***
I want To verify text on Hyperspace Animation
    [Documentation]    Test to open API Demos on an emulator
    Given Open Application To API Demos
    When I Open Views
    Then I Open Animation Page And I Click On Push Button
    And I Select Hyperspace Animation And I Check Message

I want To verify text on Chronometer
    [Documentation]    Test to open API Demos on an emulator
    Given Open Application To API Demos
    When I Open Views
    Then I Open Chronometer Page And I Click On Start Button

I Want To Verify Seekbar
    [Documentation]    e
    Given Open Application To API Demos
    When I Open Views
    Then I Open Seekbar And I Put To 88
