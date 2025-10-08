import asyncio
import sys
import os

# On s'assure que le dossier racine du projet est dans le path pour les imports
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    from telethon import TelegramClient
    from telethon.tl.types import Message
    from backend.config import API_ID, API_HASH, TELEGRAM_BOT_TOKEN, CHANNEL_IDS, SESSION_NAME
    from backend.telegram_bot.indexer import add_file
except ImportError as e:
    print(f"Erreur d'importation. Assurez-vous que les dépendances sont installées. Erreur: {e}")
    sys.exit(1)

async def process_message(message: Message, channel_name: str):
    """Traite un message et l'ajoute à la base de données s'il contient un fichier."""
    file_to_index = None
    file_type = None

    if message.document:
        file_to_index = message.document
        file_type = 'document'
    elif message.video:
        file_to_index = message.video
        file_type = 'video'
    elif message.audio:
        file_to_index = message.audio
        file_type = 'audio'

    if file_to_index:
        # On utilise le nom de fichier de l'attribut, s'il existe
        file_name = getattr(file_to_index, 'file_name', 'Fichier sans nom')
        # La description est le texte du message
        description = message.text or ""

        # On construit l'URL publique du message
        telegram_url = f"https://t.me/{message.chat.username}/{message.id}"

        add_file(
            file_name=file_name,
            description=description,
            telegram_url=telegram_url,
            file_type=file_type,
            channel_name=channel_name
        )

async def main():
    """
    Fonction principale pour lancer le processus d'indexation.
    """
    if not all([API_ID, API_HASH, TELEGRAM_BOT_TOKEN, CHANNEL_IDS]):
        print("Arrêt du script. Veuillez remplir le fichier .env avec vos informations.")
        return

    print("Lancement du bot d'indexation avec Telethon...")

    # On utilise le token de bot pour l'authentification.
    # Le fichier de session sera créé pour garder la connexion.
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

    async with client.start(bot_token=TELEGRAM_BOT_TOKEN) as bot:
        print("Client connecté avec succès.")
        for channel_id in CHANNEL_IDS:
            try:
                # On récupère l'entité du canal pour avoir son nom/username
                entity = await bot.get_entity(channel_id)
                print(f"\nAnalyse du canal : {entity.title}...")

                # On parcourt les messages du canal
                async for message in bot.iter_messages(entity, limit=200): # Limite pour la démo
                    await process_message(message, entity.title)

            except Exception as e:
                print(f"Erreur lors de l'analyse du canal {channel_id}: {e}")
                print("Veuillez vérifier que l'ID est correct et que le bot est bien membre du canal.")

    print("\nIndexation terminée.")


if __name__ == '__main__':
    asyncio.run(main())