# OC_P12 Architecture back-end sécurisée en utilisant Django ORM

Douxième projet de la formation "Développeur d'application - Python" d'OpenClassrooms dont le but est de créer une API basée sur Django REST pour un CRM.

## Pour commencer

Ces instructions vous permettent de récupérer une copie du projet pour le tester sur votre machine.

### Prerequis

Ce programme étant basé sur Python, il est nécessaire que celui-ci soit installé sur votre machine.
Vous pouvez télécharger Python [ici](https://www.python.org/downloads/)

### Installation

Pour ne pas entrer en conflit avec d'autres projets déjà existants, il est préférable d'exécuter le programme sous un environnement virtuel.

Voici les principales commandes pour:

1. créer l'environnement virtuel

```
python3 -m venv tutorial-env
```
2. activer l'environnement virtuel

```
tutorial-env\Scripts\activate.bat
```

Pour plus de détails sur l'installation d'un environnement virtuel, se reporter à [la documentation Python](https://docs.python.org/fr/3.6/tutorial/venv.html)

Il est également nécessaire d'installer les bibliothèques indispensables au bon fonctionnement du programme. 
Celles-ci sont listées dans le document `requirement.txt` et leur installation se fait via la commande suivante exécutée dans l'environnement virtuel que vous venez de créer:
```
pip install -r requirements.txt
```

## Exécution du programme

Se placer dans le dossier `/CRM_Epic_Event` de l'environnement virtuel et exécuter la commander suivante :
```
python3 manage.py runserver
```
## Tester les requêtes de l'API

Utilisez Postman


## Auteur

**Léo CAPOU** 

## Remerciements

* Tim
