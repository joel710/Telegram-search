import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

# On importe le nom de la base de données depuis notre configuration
try:
    from config import DATABASE_NAME
except ImportError:
    print("Erreur: Le fichier de configuration 'config.py' est introuvable.")
    DATABASE_NAME = 'backend/database.db' # Fallback pour la sécurité

# On initialise l'application Flask
app = Flask(__name__)
# On configure CORS pour autoriser les requêtes depuis n'importe quelle origine
CORS(app)

# --- Logique pour les vignettes par défaut ---
# On associe un type de fichier à une image par défaut.
THUMBNAIL_MAP = {
    'video': "https://images.unsplash.com/photo-1574267432553-8b448192b8c2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60",
    'audio': "https://images.unsplash.com/photo-1511379938547-c1f69419868d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60",
    'document': "https://images.unsplash.com/photo-1583344692135-453513619590?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60",
    'default': "https://images.unsplash.com/photo-1585664811087-47f65abbad64?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60"
}

def get_db_connection():
    """Crée et retourne une connexion à la base de données."""
    conn = sqlite3.connect(DATABASE_NAME)
    # Cette ligne permet de récupérer les résultats sous forme de dictionnaires
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return "Le serveur backend est en marche !"

# --- Notre route de recherche, maintenant connectée à la base de données ---
@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('q', '').strip()

    if not query:
        return jsonify([])

    conn = get_db_connection()
    cursor = conn.cursor()

    # On recherche le terme dans la description ET le nom du fichier
    search_term = f"%{query}%"
    cursor.execute(
        "SELECT file_name, description, telegram_url, file_type, channel_name FROM files WHERE description LIKE ? OR file_name LIKE ?",
        (search_term, search_term)
    )

    files = cursor.fetchall()
    conn.close()

    # On formate les résultats pour qu'ils correspondent à ce que le frontend attend
    results = []
    for file in files:
        results.append({
            "title": file['file_name'],
            "description": file['description'] or f"Fichier trouvé sur le canal {file['channel_name']}",
            "thumbnail": THUMBNAIL_MAP.get(file['file_type'], THUMBNAIL_MAP['default']),
            "url": file['telegram_url']
        })

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5001)