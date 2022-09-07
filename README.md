# Nom de repository : OC_Project_04_Repository

Projet 04 : Développez un programme logiciel en Python
 
Les étapes à suivre pour exécuter le script Python main.py relatif au projet 04 :

I. Préparation de l'environnement de travail

	1. Téléchargement et installation de la dernière version de Python (actuellement, Python 3.10.7)
		1.1. Téléchargez la dernière version de Python en utilisant l'URL https://www.python.org/downloads/
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

II. Création d'un environnement virtuel (project_env, par exemple) à l'aide du terminal "Git Bash" ou "PyCharm"

	1. Exécutez "Pycharm" ou "Git Bash" pour accéder à son terminal
	2. Accédez à votre dossier de travail ayant été déjà créé (OC_Project_04, par exemple) en exécutant la commande :
	cd OC_Project_04
	3. Tapez et exécutez la commande ci-dessous pour créer un nouveau environnement virtuel nommé project_env :
	python -m venv project_env

III. Activation et désactivation de l'environnement virtuel project_env à l'aide du terminal "Git Bash" ou "PyCharm"

	1. Activation sous MacOS ou Linux/Unix de l'environnement virtuel à l'aide du terminal "Git Bash" en exécutant :
	source project_env/bin/activate
	2. Activation sous Windows de l'environnement virtuel à l'aide du terminal "Git Bash" en exécutant la commande :
	source ./Project02_env/Scripts/activate	
	3. Activation sous Windows de l'environnement virtuel à l'aide du terminal "PyCharm" en exécutant la commande :
	project_env/Scripts/activate
	
	Dans le cas où l'environnement virtuel n'a été pas activé, vous pouvez exécuter, avant l'activation, la commande :
	Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
	Ainsi, vous pouver utiliser ces deux liens pour vous aider à résoudre ce problème :
	https://www.windows8facile.fr/powershell-execution-de-scripts-est-desactivee-activer/
	https://www.pcastuces.com/pratique/astuces/3908.htm
	
	4. Désactivation de l'environnement virtuel à l'aide du terminal "Git Bash" ou "PyCharm" en exécutant la commande :
	deactivate

IV. Récupération du repository depuis GitHub à partir du lien https://github.com/RochdiGZ/OC_Project_04_Repository

	1. Accédez au terminal "Git Bash" ou "Pycharm" pour cloner le projet en local sur votre ordinateur
	2. Tapez et Exécutez la commande ci-dessous en utilisant le lien ci-dessus
	git clone https://github.com/RochdiGZ/OC_Project_04_Repository.git 
	3. Lancez PyCharm et ouvrir le projet ajouté en local, dans le dossier de travail, et nommé OC_Project_04_Repository
    et ayant été hébergé sur GitHub et contenant les fichiers suivants :
		* README.md : contient les étapes à suivre pour exécuter le code Python relatif au projet 04
		* Requirements.txt : contient tous les paquets (packages) nécessaires à l'exécution des scripts Python
		* main.py : contient le script principal pour l'exécuter dans l'environnement virtuel project_env
		* des autres packages Python dont chacun contient des modules nécessaires pour l'exécution du script main.py

V. Exécution du script Python main.py

	1. Créez l'environnment virtuel project_env dans le dossier OC_Project04_Repository (voir paragraphe III.)
	2. Activez l'environnement virtuel project_env ayant été créé précédement (voir paragraphe III.)
	3. Accédez au terminal "Git Bash" ou "PyCharm" pour taper et exécuter la commande qui permet, tout d'abord, de
    mettre à jour le module pip :
	python -m pip install --upgrade pip
	4. Tapez et exécutez la commande qui permet d'installer tous les paquets nécessaires à l'exécution du script main.py
	pip install -r requirements.txt
	5. Finalement, exécutez le script principal main.py, dans l'environnement virtuel, en utilisant la commande :
	python main.py
		
------------------------------------------------------------------------------------------------------------------------
Pour toutes informations sur les besoins de l'exécution du script Python main.py, veuillez me contacter par email :
Rochdi.GUEZGUEZ@Gmail.Com
------------------------------------------------------------------------------------------------------------------------