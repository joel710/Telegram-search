import os
from dotenv import load_dotenv

# On charge les variables d'environnement depuis le fichier .env
# find_dotenv() cherche le fichier .env en remontant dans les dossiers parents.
load_dotenv()

# --- Configuration de l'API Telegram ---
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')

# --- Configuration du Bot Telegram ---
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# On lit les IDs des canaux, on les nettoie et on les convertit en entiers.
_channel_ids_str = os.getenv('CHANNEL_IDS', '')
CHANNEL_IDS = [int(channel_id.strip()) for channel_id in _channel_ids_str.split(',') if channel_id.strip()]

# --- Configuration de la Base de Données ---
DATABASE_NAME = 'backend/database.db'

# --- Configuration de Telethon ---
SESSION_NAME = 'backend/telegram_session'


# --- Validation ---
# On vérifie que les variables essentielles sont bien présentes.
if not all([API_ID, API_HASH, TELEGRAM_BOT_TOKEN, CHANNEL_IDS]):
    print("ERREUR : Une ou plusieurs variables d'environnement sont manquantes.")
    print("Veuillez copier .env.example en .env et le remplir avec vos informations.")
    # On pourrait vouloir quitter le script ici dans une vraie application
    # sys.exit(1)