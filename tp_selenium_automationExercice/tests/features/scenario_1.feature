# Scénario 1 :
# Le navigateur est lancé
# L'utilisateur accède à http://automationexercise.com
# L'utilisateur ajoute des produits au panier
# L'utilisateur clique sur "Procéder au paiement" et s'inscrit
# "COMPTE CRÉÉ !" est visible
# L'utilisateur finalise sa commande avec des informations de paiement valides
# Le message "Félicitations ! Votre commande a été confirmée !" est visible
# L'utilisateur clique sur "Télécharger la facture"
# La facture est téléchargée avec succès

Feature: Completing an order on AutomationExercise

  Scenario: User successfully places an order
    Given I navigate to the AutomationExercise website
    When I add products to the cart
    Then I proceed to checkout and sign up
    And the message ACCOUNT CREATED! should be visible
    And I complete the order with valid payment information
    Then the message "Congratulations! Your order has been confirmed!" should be visible
    When I click on "Download Invoice"
    Then the invoice should be downloaded successfully

