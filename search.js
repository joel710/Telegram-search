document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('searchForm');
    const searchInput = document.getElementById('searchInput');
    const resultsGrid = document.getElementById('resultsGrid');
    const noResults = document.getElementById('noResults');

    // L'URL de notre API backend.
    // On la met dans une constante pour la modifier facilement si besoin.
    const API_URL = 'http://localhost:5001/api/search';

    /**
     * Affiche les résultats de recherche dans la grille.
     * @param {Array<Object>} results - Une liste d'objets représentant les résultats.
     */
    function displayResults(results) {
        resultsGrid.innerHTML = ''; // On vide les anciens résultats

        if (results.length === 0) {
            noResults.classList.remove('hidden');
            resultsGrid.classList.add('hidden');
        } else {
            noResults.classList.add('hidden');
            resultsGrid.classList.remove('hidden');

            results.forEach(result => {
                const card = document.createElement('a');
                card.href = result.url;
                card.target = '_blank';
                card.classList.add('result-card', 'bg-gray-800', 'rounded-lg', 'overflow-hidden', 'fade-in');
                card.style.animationDelay = `${Math.random() * 0.3}s`;

                card.innerHTML = `
                    <div class="relative h-64 w-full">
                        <img src="${result.thumbnail}" alt="${result.title}" class="w-full h-full object-cover">
                        <div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black to-transparent p-4">
                            <h3 class="text-white font-semibold truncate">${result.title}</h3>
                        </div>
                    </div>
                    <div class="p-4">
                        <p class="text-gray-400 text-sm mb-3 h-10 overflow-hidden">${result.description}</p>
                        <div class="w-full bg-indigo-600 hover:bg-indigo-700 text-white py-2 rounded text-sm font-medium transition duration-300 text-center">
                            <i class="fas fa-download mr-2"></i>Voir sur Telegram
                        </div>
                    </div>
                `;
                resultsGrid.appendChild(card);
            });
        }
    }

    // On connecte le formulaire à la fonction de recherche via l'API
    searchForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const searchTerm = searchInput.value.trim();

        if (!searchTerm) {
            displayResults([]);
            return;
        }

        try {
            // On envoie la requête à notre backend
            const response = await fetch(`${API_URL}?q=${encodeURIComponent(searchTerm)}`);

            if (!response.ok) {
                // Si le serveur renvoie une erreur (ex: 500), on la lève
                throw new Error(`Erreur du serveur: ${response.statusText}`);
            }

            const results = await response.json();
            displayResults(results);

        } catch (error) {
            // Si la connexion au serveur échoue, on affiche une erreur dans la console
            // et on vide les résultats.
            console.error("Impossible de contacter le serveur de recherche :", error);
            noResults.textContent = "Erreur de connexion au serveur. Vérifiez qu'il est bien lancé.";
            displayResults([]);
        }
    });
});