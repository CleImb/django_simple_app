## Overview

Une application Django simple de démonstration. Elle permet :
* À partir de l'interface admin de Django de créer un utilisateur : `<host>/admin/`
* À un utilisateur de se loger avec une authentification simple et de modifier son adresse email, avec front en html-css : `<host>/accounts/`
* À quiquonque, grace à une structure en rest, de pouvoir récupérer, créer, modifier, supprimer directement les users : `<host>/accounts/users/`

## Quick start

* Après avoir cloner le répertoire. Créer un fichier de configuration `.env` à la racine du projet, avec les variables suivantes:

```
SECRET_KEY=<secret_key>
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DJANGO_SETTINGS_MODULE=<django_settings_module>
```

* Dans le fichier `docker-compose.yml`, spécifier un port libre dans le service `web`
* Lancer les containers dans votre environnement de travail. Pour vs code, utiliser l'extension pack `Remote Development`.
* Initialiser la base de données avec la commande Django :
`python manage.py migrate`
* Créer un superuser avec la commande Django :
`python manage.py createsuperuser`
* L'interface admin, le front de connection et l'api rest sont utilisables : `localhost:<port>/admin/`, `localhost:<port>/accounts/`, `localhost:<port>/accounts/users/`
* Afin de vérifier la qualité du code avant votre premier commit, installer pre-commit :
`pre-commit install`


## Notes

* Il n'y a pas la possibilité pour un utilisateur de créer son entrée lui-même dans la base de données à partir d'un formulaire. Pour ce faire, il faut passer par l'interface admin de Django.
* La partie front n'est pas pleinement fonctionnelle. Le clique pour la modification de l'adresse mail renvoie une erreur. Pour la corriger, il faut modifier l'appel dans le fichier html : `accounts/templates/accounts/user_detail.html`
* La partie js de ce même fichier est appeler dans le html. Elle devrait se trouver dans un fichier static à part.
* La partie rest n'a aucune sécurisation pour des faciliter de test. C'est bien sûr à changer pour une utilisation réélle.
* Les templates d'authentification sont inspirés de ceux présents dans `https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication`
* Formating avec Black
* Aucun test unitaire n'est présent.
