document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('searchForm');
    const searchInput = document.getElementById('searchInput');
    const resultsGrid = document.getElementById('resultsGrid');
    const noResults = document.getElementById('noResults');

    // --- Données d'exemple pour la simulation ---
    const sampleResults = [
        {
            title: "Exemple de Film HD",
            description: "Un film d'action et d'aventure.",
            thumbnail: "https://images.unsplash.com/photo-1574267432553-8b448192b8c2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60",
            url: "#" // Lien placeholder
        },
        {
            title: "Série TV - Saison 1",
            description: "Une série dramatique captivante.",
            thumbnail: "https://images.unsplash.com/photo-1626814026310-25d416346156?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60",
            url: "#"
        },
        {
            title: "Documentaire Nature",
            description: "Explorez la beauté de notre planète.",
            thumbnail: "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60",
            url: "#"
        },
        {
            title: "Jeu PC Complet",
            description: "Un jeu de stratégie en temps réel.",
            thumbnail: "https://images.unsplash.com/photo-1550745165-9bc0b252726a?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60",
            url: "#"
        },
        {
            title: "Album de Musique (FLAC)",
            description: "Les derniers hits en haute qualité.",
            thumbnail: "https://images.unsplash.com/photo-1511379938547-c1f69419868d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60",
            url: "#"
        }
    ];

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
                card.style.animationDelay = `${Math.random() * 0.3}s`; // Ajoute un petit décalage d'animation

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

    // On connecte le formulaire à la fonction de simulation
    searchForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const searchTerm = searchInput.value.trim().toLowerCase();

        // Simulation : si la recherche est "vide", on n'affiche aucun résultat.
        // Sinon, on affiche les résultats d'exemple.
        if (searchTerm === 'vide') {
            displayResults([]);
        } else {
            displayResults(sampleResults);
        }
    });
});