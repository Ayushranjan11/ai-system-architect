# 🤖 AI System Architect
A simple web tool that uses Google's Gemini AI to instantly convert high-level business ideas into low-level technical specifications.

# ✨ What It Does
This tool automates the initial software planning process. Simply provide a business requirement, and the AI will generate a complete technical blueprint, including:

📦 Proposed Modules: The key software components needed.

🗄️ Database Schemas: A simple table structure for the core features.

📄 Pseudocode: High-level code logic for a primary function.

# 🛠️ Tech Stack
Backend: Python & Flask

Frontend: HTML & CSS

AI: Google Gemini API

# 🚀 How to Run It Locally
Follow these simple steps to get the project running on your machine.

Clone the Repository

git clone https://github.com/Ayushranjan11/ai-system-architect.git
cd ai-system-architect

Setup Virtual Environment & Install Packages

# Create and activate the environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

Add Your API Key

Make a copy of the example environment file:

cp env.example .env

Open the new .env file and paste in your GOOGLE_API_KEY.

Run the Application

python app.py

View in Browser

Open your web browser and go to: http://127.0.0.1:5000
