# GitHub Bootcamp Contributors Page

## 🚀 Project Overview
This project is designed to help students learn Git, GitHub, and collaborative open-source development through a hands-on contributor showcase project.

## 📋 Prerequisites
- Python 3.7+
- Git
- GitHub Account
- Basic understanding of Python and JSON

## 🛠️ Project Setup

### 1. Fork the Repository
1. Navigate to the [GitHub Bootcamp Repository](https://github.com/ksauraj/GitHub-Bootcamp)
2. Click the "Fork" button in the top right corner of the page
3. Choose your personal GitHub account to create a fork

### 2. Clone Your Forked Repository
```bash
# Replace YOUR_USERNAME with your GitHub username
git clone https://github.com/YOUR_USERNAME/GitHub-Bootcamp.git
cd GitHub-Bootcamp
```

### 3. Create a Virtual Environment (Optional but Recommended)
```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On macOS and Linux
source venv/bin/activate
```

### 4. Install Dependencies
```bash
# Install required packages
pip install -r requirements.txt
```

## 🤝 How to Contribute

### Step 1: Create Your Contributor Profile
1. Navigate to the `assets/user/` directory
2. Create a new JSON file named `{your-student-id}.json`
3. Use the following template:

```json
{
    "name": "Your Full Name",
    "githubUsername": "your_github_username",
    "bio": "A short professional or personal bio",
    "pfpUrl": "https://link-to-your-profile-picture.jpg",
    "socialLinks": {
        "GitHub": "https://github.com/your_username",
        "LinkedIn": "https://linkedin.com/in/your_profile"
    }
}
```

### Step 2: Validate Your JSON
- Ensure your JSON file is valid
- Use online JSON validators if needed
- Check that all links are working

### Step 3: Generate HTML
```bash
# Run the HTML generation script
python scripts/generate_html.py
```

### Step 4: Commit and Push Changes
```bash
# Add your JSON file
git add assets/user/your-student-id.json
git add index.html

# Commit with a meaningful message
git commit -m "Add contributor profile for YOUR_NAME"

# Push to your fork
git push origin main
```

### Step 5: Create a Pull Request
1. Go to your forked repository on GitHub
2. Click "Pull Request"
3. Ensure:
   - Base repository is `ksauraj/GitHub-Bootcamp`
   - Base branch is `master`
   - Head repository is `YOUR_USERNAME/GitHub-Bootcamp`
   - Head branch is your working branch
4. Create the Pull Request
5. Add a descriptive title and comment

## 📝 Guidelines
- Use a professional tone in your bio
- Choose a clear, appropriate profile picture
- Ensure all links are working
- Follow the JSON structure exactly
- No offensive or inappropriate content

## 🛡️ Contribution Checks
Your pull request will be reviewed for:
- Valid JSON structure
- Working links
- Appropriate content
- Successful HTML generation

## 🤔 Troubleshooting
- Verify Python installation: `python3 --version`
- Check JSON validity using online validators
- Ensure all required fields are filled
- If script fails, check error messages carefully

---

**Happy Contributing! 🚀👩‍💻👨‍💻**
PR by pranayasingh
