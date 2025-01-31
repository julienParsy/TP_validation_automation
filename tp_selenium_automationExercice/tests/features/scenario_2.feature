# Le navigateur est lancé
# L'utilisateur accède à http://automationexercise.com
# L'utilisateur clique sur le bouton "Produits"
# L'utilisateur est dirigé vers la page "TOUS LES PRODUITS"
# L'utilisateur entre un nom de produit dans la barre de recherche et clique sur "Rechercher"
# "PRODUITS RECHERCHÉS" est visible
# Tous les produits correspondants sont affichés
# L'utilisateur ajoute ces produits au panier
# L'utilisateur clique sur le bouton "Panier"
# Les produits ajoutés sont visibles dans le panier
# L'utilisateur clique sur "Inscription/Connexion" et se connecte
# L'utilisateur retourne à la page Panier
# Les produits ajoutés sont toujours visibles
# L'utilisateur supprime tous les produits du panier
# Le message "Le panier est vide ! Cliquez ici pour acheter des produits." est visible


Feature: Product Search and Cart Management  

  Scenario: User searches for a product, adds it to the cart, and manages the cart  
    Given the user navigates to "http://automationexercise.com"  
    When the user clicks on the "Products" button  
    Then the user should be redirected to the "ALL PRODUCTS" page  

    When the user searches for a product by entering a name in the search bar  
    And clicks the search button  
    Then the "SEARCHED PRODUCTS" section should be visible  
    And all matching products should be displayed  

    When the user adds all displayed products to the cart  
    And clicks on the "Cart" button  
    Then the added products should be visible in the cart  

    When the user clicks on "Signup / Login" and logs in successfully  
    And navigates back to the Cart page  
    Then the previously added products should still be present  

    When the user removes all products from the cart  
    Then the message "Cart is empty! Click here to buy products." should be displayed  
