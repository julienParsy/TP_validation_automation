# Elements > Links Following links will send an api call > Vérifier tout les retours
# Forms > et remplir le formulaire
# Tool tips > Vérifier les hover
# Select menu
# Select value > another root option
# Select one > Another
# Old Style menu >  Aqua
# Drop down > toutes les couleurs 
# Multi select > Audi
# Elements >
# Radio button
# Cliquer sur tout les boutons et vérifications des messages
# Dynamic properties
# color change et vérifier le changement de couleur
# Book store application
# Créer un user et s'assurer qu'il soit créer

Feature: Validate API call links on DemoQA

  Scenario: Check response status for all API call links
    Given the user is on the DemoQA links page
    When they click on each link in the API call section
    Then they should receive a valid HTTP response code
