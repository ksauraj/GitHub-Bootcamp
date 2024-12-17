document.addEventListener('DOMContentLoaded', () => {
    const userCardsContainer = document.getElementById('userCards');
    const themeToggle = document.createElement('button');
    const htmlElement = document.documentElement;

    // Dark Mode Toggle Setup
    themeToggle.id = 'theme-toggle';
    themeToggle.className = 'bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-gray-200 px-4 py-2 rounded-full transition duration-300 hover:bg-gray-300 dark:hover:bg-gray-600';
    themeToggle.textContent = 'Toggle Theme';
    
    // Insert theme toggle before user cards
    userCardsContainer.parentElement.insertBefore(themeToggle, userCardsContainer);

    // Dark Mode Toggle Logic
    themeToggle.addEventListener('click', () => {
        htmlElement.classList.toggle('dark');
        // Save preference to localStorage
        localStorage.setItem('theme', 
            htmlElement.classList.contains('dark') ? 'dark' : 'light'
        );
    });

    // Check for saved theme preference
    if (localStorage.getItem('theme') === 'dark') {
        htmlElement.classList.add('dark');
    }

    // Function to fetch and create user cards
    async function createUserCards() {
        // Placeholder for user files - replace with actual path or dynamic loading
        const userFiles = [
            'assets/user/2300270290001.json',
            'assets/user/2300270290002.json'
            // Add more file paths as needed
        ];

        for (const filePath of userFiles) {
            try {
                const response = await fetch(filePath);
                const userData = await response.json();

                // Create card element with dark mode support
                const cardElement = document.createElement('div');
                cardElement.className = 'bg-white dark:bg-gray-800 rounded-lg shadow-lg overflow-hidden transform transition duration-300 hover:scale-105';
                
                // Construct card HTML with dark mode classes
                cardElement.innerHTML = `
                    <div class="p-6 text-center">
                        <img src="${userData.pfpUrl || 'https://via.placeholder.com/150'}" 
                             alt="${userData.name}'s profile picture" 
                             class="w-32 h-32 rounded-full mx-auto mb-4 object-cover border-4 border-gray-200 dark:border-gray-600">
                        
                        <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200 mb-2">
                            ${userData.name}
                        </h2>
                        
                        <p class="text-gray-600 dark:text-gray-400 mb-4">
                            @${userData.githubUsername}
                        </p>
                        
                        <p class="text-sm text-gray-500 dark:text-gray-500 italic">
                            ${userData.bio || 'No bio provided'}
                        </p>

                        <div class="flex justify-center mt-4 space-x-3">
                            ${Object.entries(userData.socialLinks || {})
                                .map(([platform, link]) => `
                                    <a href="${link}" class="text-gray-600 dark:text-gray-400 hover:text-blue-500 dark:hover:text-blue-400">
                                        <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                                            <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                                        </svg>
                                    </a>
                                `).join('')}
                        </div>
                    </div>
                `;

                userCardsContainer.appendChild(cardElement);
            } catch (error) {
                console.error(`Error loading user file ${filePath}:`, error);
            }
        }
    }

    // Call the function to create cards
    createUserCards();
});
