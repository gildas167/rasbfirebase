# rasbfirebase

# Envoi de Données à Firebase depuis un Raspberry Pi

Ce projet montre comment configurer un Raspberry Pi pour envoyer des données à une base de données Firebase en utilisant Python.

## Prérequis

- **Raspberry Pi** avec Python installé.
- **Compte Firebase** et projet configuré.

## 1. Préparer l'Environnement Firebase

### Créer un Projet Firebase

1. Connecte-toi à [la console Firebase](https://console.firebase.google.com/).
2. Crée un nouveau projet ou utilise un projet existant.
3. Accède à **Base de données** et clique sur **Créer une base de données**.
4. Choisis le **Mode Test** pour une configuration initiale plus simple.

### Générer une Clé de Service

1. Dans **Paramètres du projet**, va à l'onglet **Comptes de service**.
2. Clique sur **Générer une nouvelle clé privée**.
3. Télécharge le fichier JSON des informations d'identification du compte de service.

## 2. Configurer l'Accès à Firebase sur le Raspberry Pi

### Installer les Dépendances

1. Ouvre un terminal sur ton Raspberry Pi.
2. Mets à jour les paquets :

    ```bash
    sudo apt update
    sudo apt upgrade
    ```

3. Installe Python et pip (si ce n'est pas déjà fait) :

    ```bash
    sudo apt install python3 python3-pip
    ```

4. Installe la bibliothèque Firebase Admin pour Python :

    ```bash
    pip3 install firebase-admin
    ```

### Transférer le Fichier JSON

1. Transfère le fichier JSON de Firebase vers ton Raspberry Pi. Utilise `scp`, `sftp`, ou télécharge directement sur le Raspberry Pi.
2. Place le fichier dans un répertoire approprié, par exemple `/home/pi/`.

## 3. Écrire et Exécuter un Script Python pour Envoyer des Données

### Exemple de Script Python

Crée un fichier nommé `firebase_send.py` avec le contenu suivant :

```python
import firebase_admin
from firebase_admin import credentials, db

# Chemin vers le fichier JSON téléchargé depuis Firebase
cred = credentials.Certificate('/home/pi/firebase-adminsdk.json')

# Initialiser l'application Firebase
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://<YOUR_PROJECT_ID>.firebaseio.com'
})

# Référence à la base de données
ref = db.reference('/path/to/data')  # Remplace par le chemin approprié dans ta base de données

# Envoi de données à Firebase
ref.set({
    'name': 'Raspberry Pi',
    'status': 'connected',
    'temperature': 23.5
})

print("Les données ont été envoyées à Firebase.")
