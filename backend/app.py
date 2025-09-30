from flask import Flask, jsonify, request
from flask_cors import CORS

# On initialise l'application Flask
app = Flask(__name__)
# On configure CORS pour autoriser les requêtes depuis n'importe quelle origine
CORS(app)

# --- Données d'exemple pour la simulation ---
# Ces données seront remplacées plus tard par de vrais résultats de recherche
sample_results = [
    {
        "title": "Exemple de Film HD",
        "description": "Un film d'action et d'aventure.",
        "thumbnail": "https://images.unsplash.com/photo-1574267432553-8b448192b8c2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60",
        "url": "#"
    },
    {
        "title": "Série TV - Saison 1",
        "description": "Une série dramatique captivante.",
        "thumbnail": "https://images.unsplash.com/photo-1626814026310-25d416346156?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60",
        "url": "#"
    },
    {
        "title": "Documentaire Nature",
        "description": "Explorez la beauté de notre planète.",
        "thumbnail": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60",
        "url": "#"
    },
    {
        "title": "Jeu PC Complet",
        "description": "Un jeu de stratégie en temps réel.",
        "thumbnail": "https://images.unsplash.com/photo-1550745165-9bc0b252726a?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60",
        "url": "#"
    },
    {
        "title": "Album de Musique (FLAC)",
        "description": "Les derniers hits en haute qualité.",
        "thumbnail": "https://images.unsplash.com/photo-1511379938547-c1f69419868d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60",
        "url": "#"
    }
]

@app.route('/')
def index():
    return "Le serveur backend est en marche !"

# --- Notre nouvelle route pour la recherche ---
@app.route('/api/search', methods=['GET'])
def search():
    # On récupère le terme de recherche de l'URL (ex: /api/search?q=test)
    query = request.args.get('q', '')

    # Simulation : si la recherche est "vide", on renvoie une liste vide.
    # Sinon, on renvoie les résultats d'exemple.
    if query.lower() == 'vide':
        return jsonify([])
    else:
        return jsonify(sample_results)

if __name__ == '__main__':
    app.run(debug=True, port=5001)