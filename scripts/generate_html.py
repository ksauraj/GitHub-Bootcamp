import os
import json
import glob

def generate_user_cards_html():
    """
    Generate a complete HTML file with user cards, dark mode, and dynamic loading
    """
    # Path to the user JSON files
    user_dir = 'assets/user'
    
    # Output HTML file
    output_file = 'index.html'
    
    # Collect user card data
    user_cards_data = []
    
    # Find all JSON files in the directory
    json_files = glob.glob(os.path.join(user_dir, '*.json'))
    
    for file_path in json_files:
        try:
            with open(file_path, 'r') as f:
                user_data = json.load(f)
                user_cards_data.append(user_data)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    # Full HTML template with embedded JavaScript and CSS
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en" class="dark">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Project Contributors</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <script>
            tailwind.config = {{
                darkMode: 'class'
            }}
        </script>
        <style>
            body {{
                transition: background-color 0.3s, color 0.3s;
            }}
        </style>
    </head>
    <body class="bg-gray-100 dark:bg-gray-900 text-gray-900 dark:text-gray-100 min-h-screen">
        <div class="container mx-auto px-4 py-8">
            <div class="flex justify-between items-center mb-8">
                <h1 class="text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-purple-400 via-pink-500 to-red-500 dark:from-purple-300 dark:via-pink-400 dark:to-red-400">
                    Project Contributors
                </h1>
                <button id="theme-toggle" class="bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-gray-200 px-4 py-2 rounded-full transition duration-300 hover:bg-gray-300 dark:hover:bg-gray-600">
                    Toggle Theme
                </button>
            </div>

            <div id="userCards" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
                <!-- User cards will be dynamically inserted here -->
            </div>
        </div>

        <script>
            // Predefined user data from Python generation
            const USERS = {json.dumps(user_cards_data)};

            // Dark Mode Toggle
            const themeToggle = document.getElementById('theme-toggle');
            const htmlElement = document.documentElement;
            const userCardsContainer = document.getElementById('userCards');

            // Theme toggling logic
            themeToggle.addEventListener('click', () => {{
                htmlElement.classList.toggle('dark');
                localStorage.setItem('theme', 
                    htmlElement.classList.contains('dark') ? 'dark' : 'light'
                );
            }});

            // Initialize theme from localStorage
            if (localStorage.getItem('theme') === 'dark') {{
                htmlElement.classList.add('dark');
            }}

            // Function to create user cards
            function createUserCard(user) {{
                const cardDiv = document.createElement('div');
                cardDiv.className = 'bg-white dark:bg-gray-800 rounded-lg shadow-lg overflow-hidden transform transition duration-300 hover:scale-105';
                
                // Social links HTML generation
                const socialLinksHTML = user.socialLinks 
                    ? Object.entries(user.socialLinks)
                        .map(([platform, url]) => `
                            <a href="${{url}}" target="_blank" class="text-gray-600 dark:text-gray-400 hover:text-blue-500 dark:hover:text-blue-400 mx-2">
                                ${{platform}}
                            </a>
                        `)
                        .join('') 
                    : '';

                cardDiv.innerHTML = `
                    <div class="p-6 text-center">
                        <img 
                            src="${{user.pfpUrl || 'https://via.placeholder.com/150'}}" 
                            alt="${{user.name}}'s profile picture"
                            class="w-32 h-32 rounded-full mx-auto mb-4 object-cover border-4 border-gray-200 dark:border-gray-600"
                        >
                        <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200 mb-2">
                            ${{user.name}}
                        </h2>
                        <p class="text-gray-600 dark:text-gray-400 mb-4">
                            @${{user.githubUsername}}
                        </p>
                        <p class="text-sm text-gray-500 dark:text-gray-500 italic mb-4">
                            ${{user.bio || 'No bio provided'}}
                        </p>
                        <div class="flex justify-center mt-4">
                            ${{socialLinksHTML}}
                        </div>
                    </div>
                `;

                return cardDiv;
            }}

            // Render all user cards
            USERS.forEach(user => {{
                userCardsContainer.appendChild(createUserCard(user));
            }});
        </script>
    </body>
    </html>
    """
    
    # Write the HTML file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    print(f"Generated {output_file} with {len(user_cards_data)} user cards.")

# Run the script
if __name__ == '__main__':
    generate_user_cards_html()
