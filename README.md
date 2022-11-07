# Nom Repository : OC_Project_04_Repository

Projet 04 : Développez un programme logiciel en Python (Développez une application pour gérer un tournoi d'échecs)

A. Description de l'application "Chess Tournament"

C'est une application Python hors ligne correspondant au code main.py qui s'exécute dans le terminal.
Elle a pour but de gérer le déroulement des tournois organisés par un club d'échecs.
Ces tournois doivent suivre le système suisse pour générer les paires de joueurs de chaque ronde d'un tournoi afin que:
les matchs soient équitables et ne se reproduisent pas.

En effet, cette application permet de :
* ajouter des joueurs dans une base de données correspondant au fichier chess_db.json,
* modifier les classemnts des joueurs en modifiant la base de données,
* créer et commencer un nouveau tournoi en modifiant la base de données,
* sélectionner et reprendre un tournoi existant en modifiant la base de données,
* afficher des rapports qui correspondent chacun à :
    - la liste de tous les joueurs existants dans la base de données par ordre,
    - la liste de tous les tournois existants dans la base de données par ordre,
    - la liste de tous les participants par ordre,
    - la liste de tous les matches de rondes d'un tournoi existant dans la base de données.

B. Structure du code en utilisant le design pattern MVC
La structure de l'application suit le modèle de conception MVC (Modèle-Vue-Contrôlleur).
Cette structure contient le dossier flake8_report contenant le fichier html index.html généré par la commande:
flake8 --format=html --htmldir=flake8_report --max-line-length=119
Ce fichier html peut être lancé par un navigateur web et contient un message indiquant que:
la structure du code de l'application ne contient pas des erreurs.
Le module flake8 doit être installé à l'aide de la commande:
pip install flake8=4.0.1

C. Les étapes à suivre pour exécuter le script Python main.py relatif au projet 04 :

I. Préparation de l'environnement de travail

	1. Téléchargement et installation de la version 3.10 de Python
		1.1. Téléchargez la version 3.10 de Python en utilisant l'URL https://www.python.org/downloads/
		et en choisissant votre système Windows, macOS ou Linux/Unix
		1.2. Cliquez sur le lien de téléchargement
		1.3. Installez cette version de Python qui dispose du module venv.
             Par contre, la version < 3.3 ne dispose pas de venv.
		
	2. Téléchargement et installation de la dernière version de Git (Gestionnaire de versions de paquets)
		2.1. Téléchargez la dernière version de Git en utilisant l'URL https://git-scm.com/downloads/
		et en choisissant votre système Windows, macOS ou Linux/Unix
		2.2. Cliquez sur le lien de téléchargement
		2.3. Installez cette version de Git qui dispose d'un terminal Git Bash
		
	3. Téléchargement et installation de la dernière version de PyCharm
		3.1. Téléchargez la dernière version de PyCharm en utilisant l'URL https://www.jetbrains.com/fr-fr/pycharm/
		3.2. Cliquez sur le bouton Télécharger
		3.3. Choisissez votre système Windows, macOS ou Linux/Unix
		3.4. Cliquez sur le bouton Télécharger de la version gratuite Community pour le développement Python pur
		3.5. Installez cette version de PyCharm qui dispose de Git : gestionnaire de versions de paquets.
             PyCharm dispose aussi d'un terminal PS (PowerShell) similaire au terminal "Windows PowerShell"

II. Création d'un environnement virtuel (env, par exemple) à l'aide du terminal "Git Bash" ou "PyCharm"

	1. Exécutez "Pycharm" ou "Git Bash" pour accéder à son terminal
	2. Accédez à votre dossier de travail ayant été déjà créé (OC_Project_04, par exemple) en exécutant la commande :
	cd OC_Project_04
	3. Tapez et exécutez la commande ci-dessous pour créer un nouveau environnement virtuel nommé env:
	python -m venv env

III. Activation et désactivation de l'environnement virtuel à l'aide du terminal "Git Bash" ou "PyCharm"

	1. Activation sous MacOS ou Linux/Unix de l'environnement virtuel à l'aide du terminal "Git Bash" en exécutant:
	source env/bin/activate
	2. Activation sous Windows de l'environnement virtuel à l'aide du terminal "Git Bash" en exécutant la commande:
	source ./env/Scripts/activate	
	3. Activation sous Windows de l'environnement virtuel à l'aide du terminal "PyCharm" en exécutant la commande:
	env/Scripts/activate
	
	Dans le cas où l'environnement virtuel n'a été pas activé, vous pouvez exécuter, avant l'activation, la commande:
	Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
	Ainsi, vous pouver utiliser ces deux liens pour vous aider à résoudre ce problème :
	https://www.windows8facile.fr/powershell-execution-de-scripts-est-desactivee-activer/
	https://www.pcastuces.com/pratique/astuces/3908.htm
	
	4. Désactivation de l'environnement virtuel à l'aide du terminal "Git Bash" ou "PyCharm" en exécutant la commande:
	deactivate

IV. Récupération du repository depuis GitHub à partir du lien https://github.com/RochdiGZ/OC_Project_04_Repository

	1. Accédez au terminal "Git Bash" ou "Pycharm" pour cloner le projet en local sur votre ordinateur
	2. Tapez et exécutez la commande ci-dessous en utilisant le lien ci-dessus
	git clone https://github.com/RochdiGZ/OC_Project_04_Repository.git 
	3. Lancez PyCharm et ouvrir le projet ajouté en local, dans le dossier de travail, nommé OC_Project_04_Repository
    et ayant été hébergé sur GitHub et contenant les fichiers suivants :
		* README.md : contient les étapes à suivre pour exécuter le code Python relatif au projet 04
		* Requirements.txt : contient tous les paquets (packages) nécessaires à l'exécution des scripts Python
		* main.py : contient le script principal pour l'exécuter dans l'environnement virtuel env
		* des autres packages Python dont chacun contient des modules nécessaires pour l'exécution du script main.py

V. Exécution du script Python main.py

	1. Créez l'environnment virtuel env dans le dossier OC_Project04_Repository (voir paragraphe III.)
	2. Activez l'environnement virtuel env ayant été créé précédement (voir paragraphe III.)
	3. Accédez au terminal "Git Bash" ou "PyCharm" pour taper et exécuter la commande qui permet, tout d'abord, de
    mettre à jour le module pip :
	python -m pip install --upgrade pip
	4. Tapez et exécutez la commande qui permet d'installer les paquets nécessaires à l'exécution du script main.py
	pip install -r requirements.txt
	5. Finalement, exécutez le script principal main.py, dans l'environnement virtuel, en utilisant la commande :
	python main.py
		
------------------------------------------------------------------------------------------------------------------------
Pour toutes informations sur les besoins de l'exécution du script Python main.py, veuillez me contacter par email :
Rochdi.GUEZGUEZ@Gmail.Com
------------------------------------------------------------------------------------------------------------------------