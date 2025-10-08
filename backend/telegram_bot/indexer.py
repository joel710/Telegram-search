import sqlite3
import sys
import os

# On s'assure que le dossier racine du projet est dans le path pour les imports
# C'est une manière plus robuste de gérer les imports
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    from backend.config import DATABASE_NAME
except ImportError:
    print("Erreur: Le fichier de configuration 'backend/config.py' est introuvable ou mal configuré.")
    sys.exit(1)

def add_file(file_name, description, telegram_url, file_type, channel_name):
    """
    Ajoute les informations d'un fichier à la base de données.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT OR IGNORE INTO files (file_name, description, telegram_url, file_type, channel_name)
            VALUES (?, ?, ?, ?, ?)
        """, (file_name, description, telegram_url, file_type, channel_name))

        conn.commit()

        if cursor.rowcount > 0:
            print(f"Fichier ajouté : {file_name} depuis {channel_name}")
            return True
        else:
            return False

    except sqlite3.Error as e:
        print(f"Erreur de base de données lors de l'ajout du fichier : {e}")
        return False
    finally:
        if conn:
            conn.close()