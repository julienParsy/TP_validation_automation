# Dynamic properties
# color change et vérifier le changement de couleur

Feature: Dynamic properties buttons

  Scenario: Test visibility of a button after delay
    Given I navigate to the "Dynamic Properties" page
    When I wait for 5 seconds
    Then the "Visible After 5 Seconds" button should be visible

  Scenario: Test color change of a button
    Given I navigate to the "Dynamic Properties" page
    When I wait for the color change
    Then the button color should change

  Scenario: Test disabled button
    Given I navigate to the "Dynamic Properties" page
    When I wait for the "Button to be enabled"
    Then the "Enable Button" should be clickable
