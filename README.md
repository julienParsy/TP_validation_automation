# TP de validation automatisation

## Préambule

## SELENIUM

### Lancement du test

Pour lancer le test:

```POWERSHELL
 pytest tests/test_name.py
```

Pour lancer le test avec le logger:

```POWERSHELL
pytest tests/test_name.py -o log_cli=true --log-cli-level=INFO``
```

### Prérequis pour Selenium

Pour installer Python, utilisez :

👉 <https://www.python.org/downloads/>

Une fois l'installation terminée, ferme le terminal et rouvre un nouveau.

Teste Python avec :

```POWERSHELL
python --version
pip --version
```

Pour updater Python et pip, utilisez :

```POWERSHELL
python.exe -m pip install --upgrade pip
```

Si Python est bien installé, installe pytest et Selenium avec :

```POWERSHELL
pip install --upgrade pip pytest selenium webdriver-manager colorlog pytest-bdd
```

Vérifier que pytest fonctionne avec :

```POWERSHELL
pytest --version
```

### Assurez vous de disposer de la dernière version de ChromeDriver compatible avec votre version de Chrome

Pour installer et utiliser la dernière version de ChromeDriver, voici les étapes à suivre :

1. Télécharger le ChromeDriver : Rendez-vous sur la page de téléchargement de ChromeDriver et téléchargez la version compatible avec votre version de Chrome.

2. Décompresser le fichier : Extrayez le contenu du fichier téléchargé (généralement un fichier .zip).

3. Déplacer le fichier ChromeDriver : Placez le fichier chromedriver.exe dans un répertoire de votre choix. Il peut être utile de le placer dans un répertoire accessible de manière globale pour éviter d'avoir à spécifier le chemin complet à chaque fois.

4. Ajouter le répertoire au PATH : Pour que Selenium puisse trouver ChromeDriver, ajoutez le répertoire contenant chromedriver.exe à votre variable d'environnement PATH.

5. Sur Windows :

   * Ouvrez les Paramètres du système (Cliquez droit sur "Ce PC" > "Propriétés" > "Paramètres système avancés").
   * Cliquez sur Variables d'environnement.
   * Dans la section Variables système, trouvez et sélectionnez la variable Path, puis cliquez sur Modifier.
   * Ajoutez le chemin complet du répertoire contenant chromedriver.exe (par exemple, C:\path\to\chromedriver\) et cliquez sur OK.

6. Sur macOS/Linux :

   * Ouvrez le terminal.
   * Ajoutez la ligne suivante à votre fichier ~/.bash_profile, ~/.bashrc, ou ~/.zshrc (selon le shell que vous utilisez) :

```bash
        export PATH=$PATH:/chemin/vers/chromedriver
```

* Remplacez /chemin/vers/chromedriver par le chemin réel vers chromedriver.
  * Rechargez le fichier de configuration du shell en exécutant :

```bash
        source ~/.bash_profile  # ou ~/.bashrc ou ~/.zshrc
```

7. Vérifiez l'installation : Vous pouvez vérifier que ChromeDriver est correctement installé en ouvrant un terminal ou une invite de commande et en exécutant :

```bash
        chromedriver --version
```

## ROBOTFRAMEWORK

### Prérequis pour RobotFramework

Pour installer RobotFramework, utilisez :

````Powershell
pip install robotframework
pip install robotframework-browser
pip install robotframework-robocop
rfbrowser init --with-deps chromium
pip install robotframework-seleniumlibrary
pip install robotframework-faker
````
