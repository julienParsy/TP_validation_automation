# Select menu
 
# Select value > another root option
# Select one > Another
# Old Style menu >  Aqua
# Drop down > toutes les couleurs 
# Multi select > Audi

Feature: Select Menu

  Scenario: Select value another root option
    Given the user navigates to the select menu page
    When they select Another Root option from the Select value dropdown
    Then Another root option should be displayed

#   Scenario: Select one > Another
#     Given the user navigates to the select menu page
#     When they select "Select One" dropdown
#     Then "Another" should be displayed

#   Scenario: Old Style menu > Aqua
#     Given the user navigates to the select menu page
#     When they select "Old Style" dropdown
#     Then "Aqua" should be displayed

#   Scenario: Drop down > all colors
#     Given the user navigates to the select menu page
#     When they select "Drop down" dropdown
#     Then all colors should be displayed

#   Scenario: Multi select > Audi
#     Given the user navigates to the select menu page
#     When they select "Multi select" dropdown
#     Then "Audi" should be selected
