import sqlite3
import os

# On s'assure que les chemins sont corrects
BACKEND_DIR = 'backend'
DB_NAME = os.path.join(BACKEND_DIR, 'database.db')
SCHEMA_NAME = os.path.join(BACKEND_DIR, 'schema.sql')

def setup_database_for_test():
    """
    Initialise la base de données à partir du schéma et la remplit avec des données de test.
    """
    print("--- Démarrage de la configuration de la base de données de test ---")

    # --- Étape 1: Initialisation de la base de données ---
    print(f"Initialisation de la base de données '{DB_NAME}'...")
    conn = None  # On initialise la connexion à None
    try:
        # On se connecte (le fichier sera créé s'il n'existe pas)
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # On lit le schéma
        with open(SCHEMA_NAME, 'r') as f:
            schema = f.read()

        # On exécute le schéma pour (re)créer la table
        cursor.executescript(schema)
        print("Table 'files' créée avec succès.")
        conn.commit()

    except (sqlite3.Error, FileNotFoundError) as e:
        print(f"Une erreur est survenue lors de l'initialisation : {e}")
        if conn:
            conn.close()
        return # On arrête si l'initialisation échoue

    # --- Étape 2: Remplissage avec des données de test ---
    print("\nInsertion des données de test...")
    try:
        # Données de test
        test_data = [
            ('Test Video.mp4', 'Ceci est la description de ma vidéo de test.', 'https://t.me/c/12345/10', 'video', 'Canal de Test'),
            ('Document Important.pdf', 'Un document PDF pour tester la recherche.', 'https://t.me/c/12345/11', 'document', 'Canal de Test'),
            ('Musique de Test.mp3', 'Un fichier audio pour la simulation.', 'https://t.me/c/12345/12', 'audio', 'Autre Canal')
        ]

        cursor.executemany("""
            INSERT INTO files (file_name, description, telegram_url, file_type, channel_name)
            VALUES (?, ?, ?, ?, ?)
        """, test_data)

        conn.commit()
        print(f"{cursor.rowcount} lignes insérées avec succès.")

    except sqlite3.Error as e:
        print(f"Une erreur est survenue lors de l'insertion : {e}")
    finally:
        if conn:
            conn.close()
            print("\nConnexion à la base de données fermée.")

    print("--- Configuration de la base de données de test terminée ---")


if __name__ == '__main__':
    setup_database_for_test()