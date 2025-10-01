import sqlite3
import os

# Le script est exécuté depuis la racine, on doit donc spécifier le chemin du dossier backend.
BACKEND_DIR = 'backend'
DB_NAME = os.path.join(BACKEND_DIR, 'database.db')
SCHEMA_NAME = os.path.join(BACKEND_DIR, 'schema.sql')

print(f"Initialisation de la base de données '{DB_NAME}'...")

try:
    # On se connecte à la base de données (le fichier sera créé s'il n'existe pas)
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # On ouvre le fichier schema.sql et on lit son contenu
    with open(SCHEMA_NAME, 'r') as f:
        schema = f.read()

    # On exécute le script SQL pour créer la table
    cursor.executescript(schema)
    print("Table 'files' créée avec succès.")

    # On sauvegarde les changements
    connection.commit()

except (sqlite3.Error, FileNotFoundError) as e:
    print(f"Une erreur est survenue lors de l'initialisation de la base de données : {e}")

finally:
    # On ferme la connexion
    if 'connection' in locals() and connection:
        connection.close()
        print("Connexion à la base de données fermée.")