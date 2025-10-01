import sqlite3
import os

print(f"--- Début du script de débogage ---")
print(f"Répertoire de travail actuel : {os.getcwd()}")

# On liste le contenu du répertoire courant
print("\nContenu du répertoire courant :")
try:
    for item in os.listdir('.'):
        print(f"- {item}")
except FileNotFoundError:
    print("  (Répertoire courant introuvable)")


# On liste le contenu du répertoire backend
print("\nContenu du répertoire backend :")
try:
    for item in os.listdir('backend'):
        print(f"- {item}")
except FileNotFoundError:
    print("  (Répertoire backend introuvable)")

print("\n--- Fin du script de débogage ---\n")


# On s'assure que le chemin vers la base de données est correct
DB_PATH = os.path.join('backend', 'database.db')

def populate_database():
    """Ajoute des données de test à la base de données."""
    print(f"Tentative de connexion à la base de données : {DB_PATH}")

    if not os.path.exists(DB_PATH):
        print(f"ERREUR : Le fichier de base de données '{DB_PATH}' n'a pas été trouvé.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Données de test
    test_data = [
        ('Test Video.mp4', 'Ceci est la description de ma vidéo de test.', 'https://t.me/c/12345/10', 'video', 'Canal de Test'),
        ('Document Important.pdf', 'Un document PDF pour tester la recherche.', 'https://t.me/c/12345/11', 'document', 'Canal de Test'),
        ('Musique de Test.mp3', 'Un fichier audio pour la simulation.', 'https://t.me/c/12345/12', 'audio', 'Autre Canal')
    ]

    print("Insertion des données de test...")
    try:
        cursor.executemany("""
            INSERT OR IGNORE INTO files (file_name, description, telegram_url, file_type, channel_name)
            VALUES (?, ?, ?, ?, ?)
        """, test_data)

        conn.commit()
        print(f"{cursor.rowcount} lignes insérées avec succès.")

    except sqlite3.Error as e:
        print(f"Une erreur est survenue lors de l'insertion : {e}")
    finally:
        conn.close()
        print("Connexion à la base de données fermée.")

if __name__ == '__main__':
    populate_database()