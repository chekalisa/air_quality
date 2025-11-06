# 🌍 ClimAdventure

## 🇬🇧 English Version
---
**ClimAdventure** is an interactive app for travelers who care about their health and the environment.  
It helps you choose destinations with cleaner air, adapt your activities to pollution levels, and plan responsible, data-driven trips.

### Description
Plan your trips while breathing fresh air!  
ClimAdventure allows you to:
- Visualize global air pollution levels (NO₂, CO, PM2.5...) on a dynamic interactive map.  
- Discover destinations with optimal air quality.  
- Receive health and eco-friendly travel advice.  
- Access information about your destination and the best nearby hotels.  

### ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/chekalisa/air_quality.git
   
2. Navigate to the project directory:
```bash
cd air_quality
```
3. Build the Docker image:
```bash
docker build -t climaventure:latest .
```

This command uses the Dockerfile to create an image containing all required dependencies.

### Note
If you rebuild the image, make sure to remove existing containers before restarting the app.

## 🇫🇷 Version Française
---

ClimAdventure est un outil interactif pour les voyageurs soucieux de leur santé et de l'environnement. 
Cette application vous permet de choisir des destinations avec un air plus sain, d'adapter vos activités 
en fonction des niveaux de pollution, et de planifier des voyages informés et responsables.

## Description

Planifiez vos voyages en respirant l'air du large !

ClimAdventure vous aide à :

- Visualiser les niveaux de pollution (NO2, CO, PM2.5...) partout dans le monde sur une carte dynamique.
- Trouver des destinations avec une qualité de l'air optimale.
- Adopter des comportements responsables pour préserver votre santé et l'environnement.
- Trouver des infos pertinentes sur votre destination et le meilleur hôtel. 

## Installation
1. Clonez le répértoire de l'application :
 ```bash
 git clone https://github.com/chekalisa/air_quality.git
 ```
2. Accédez au répertoire du projet
```bash
cd air_quality
```
3. Créez l'image Docker
```bash
docker build -t climaventure:latest .
```
Cette commande utilise le fichier Dockerfile dans le projet pour créer une image contenant toutes les dépendances nécessaires.

## Lancement 

Démarrez le conteneur Docker
```bash
docker run -p 5001:5001 climaventure
```
Cette commande démarre l'application, qui sera accessible via un lien externe généré par Docker

### Note

Si vous voulez créer une nouvelle image docker et relancer l'application, faites attention à bien supprimer vos conteneurs une fois l’appliсation est fermée

## Auteurs

- [Alisa Chekalina](https://github.com/chekalisa)
- [Lia Gasparin](https://github.com/LiaGasparin)
- [Carmen Cristea](https://github.com/CarmenParis)
- [Vo Nguyen Thao Nhi](https://github.com/vonguyenthaonhi)

