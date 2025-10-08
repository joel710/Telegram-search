-- Supprime la table si elle existe déjà pour éviter les erreurs lors de la réinitialisation.
DROP TABLE IF EXISTS files;

-- Crée la table `files` pour stocker les informations sur les fichiers indexés.
CREATE TABLE files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_name TEXT NOT NULL,
    description TEXT,
    telegram_url TEXT NOT NULL UNIQUE,
    file_type TEXT,
    channel_name TEXT NOT NULL,
    indexed_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);