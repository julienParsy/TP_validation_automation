# Forms > et remplir le formulaire

Feature: Contact Form Validation
  As a visitor
  I want to ensure that the contact form is functional

  Scenario: Verify the presence of the contact form
      Given I am on the contact page
      When I want to fill in the required fields
      Then I should be able to fill in all fields
      And I should be able to submit the form
