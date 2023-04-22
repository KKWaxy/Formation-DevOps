# TP Docker et Docker Compose pour un projet Spring Boot Java

## Objectif :

Mettre en place une architecture microservices pour une application Spring Boot qui utilise une base de données MySQL et un serveur de messagerie Kafka, le tout avec Docker et Docker Compose.

## Étapes :

1. Créer un fichier **```Dockerfile```** pour l'application Spring Boot qui contient les instructions pour construire une image Docker pour l'application.

2. Créer un fichier **```docker-compose.yml```** qui contient les services pour l'application Spring Boot, la base de données MySQL et le serveur de messagerie Kafka.

3. Démarrer les services avec la commande **```docker-compose up```**.

4. Accéder à l'application à l'adresse **```http://localhost:8080```** et vérifier qu'elle fonctionne correctement.

5. Arrêter les services avec la commande **```docker-compose down```**.

# Bonus :

- Ajouter un service pour un cache Redis et mettre en place une configuration de cache pour l'application Spring Boot.
- Utiliser Traefik comme reverse-proxy pour l'application et configurer les règles d'acheminement pour chaque service.

# Architecure Overview

["Architecture Overview"](docs/ArchitecureOverview.png)