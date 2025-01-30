# Radio button
# Cliquer sur tout les boutons et vérifications des messages
 
Feature: Radio Button Interaction

  Scenario: Click on all radio buttons and verify the messages
    Given I am on the "Radio Button" page
    When I click on the "Yes" radio button
    Then I should see the message "Radio button Yes is checked"
    And I click on the "Impressive" radio button
    And I should see the message "Radio button Impressive is checked"
    And I verify that the "No" radio button is disabled
