import firebase_admin
from firebase_admin import credentials, db

# Chemin vers le fichier JSON téléchargé depuis Firebase
cred = credentials.Certificate("/home/pi/firebase-adminsdk.json")

# Initialisation de l'application Firebase
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://<YOUR_PROJECT_ID>.firebaseio.com'
})

# Référence à la base de données
ref = db.reference('/path/to/data')  # Remplace par le chemin approprié dans ta structure de base de données

# Envoi de données à Firebase
ref.set({
    'name': 'Raspberry Pi',
    'status': 'connected',
    'temperature': 23.5
})

print("Les données ont été envoyées à Firebase.")
