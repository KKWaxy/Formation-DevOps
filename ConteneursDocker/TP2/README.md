# TP Docker et Docker Compose pour un projet Python Django

## Objectif :

Mettre en place une architecture microservices pour une application Django qui utilise une base de données PostgreSQL et une file d'attente Redis, le tout avec Docker et Docker Compose.

## Étapes :

1. Créer un fichier **```Dockerfile```** pour l'application Django qui contient les instructions pour construire une image Docker pour l'application.

2. Créer un fichier **```docker-compose.yml```** qui contient les services pour l'application Django, la base de données PostgreSQL et la file d'attente RabbitMQ.

3. Démarrer les services avec la commande **```docker-compose up```**.

4. Accéder à l'application à l'adresse **```http://localhost:8000```** et vérifier qu'elle fonctionne correctement.

5. Arrêter les services avec la commande **```docker-compose down```**.


## Bonus :

- Ajouter un service pour un cache Memcache et mettre en place une configuration de cache pour l'application Django.
- Utiliser Traefik comme reverse-proxy pour l'application et configurer les règles d'acheminement pour chaque service.

# Architecure Overview

["Architecture Overview"](docs/ArchitectureOverview.png)

![Achitecture](/TP2/docs/ArchitectureOverview.png)