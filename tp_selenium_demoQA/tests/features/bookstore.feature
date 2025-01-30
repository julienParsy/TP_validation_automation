
Feature: Bookstore register and login
    Scenario: Accès à l'application Book Store
        Given I am on the Book Store application
        When I register with a valid username and password
        Then I should be able to login with my credentials