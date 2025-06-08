import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# --- Configure the Google Gemini API ---
try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
except Exception as e:
    print(f"[FATAL ERROR] Could not configure Google API: {e}")
    exit()

# Initialize the Flask App
app = Flask(__name__)

def generate_technical_specs(requirement):
    """Uses Gemini AI to convert a high-level requirement into technical specs."""
    print(f"[INFO] Generating specs for: '{requirement}'")
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f"""
    You are a professional System Architect. Your task is to analyze the following high-level business requirement and break it down into low-level technical specifications.

    **Business Requirement:**
    "{requirement}"

    **Your Output:**
    Provide a detailed breakdown in three distinct sections, using Markdown for formatting:

    ### 1. Proposed Modules
    List and briefly describe the key software modules or components needed to build this system (e.g., User Authentication, Notification Service, etc.).

    ### 2. Database Schema Design
    Propose a simple database schema for the core features. Describe the tables and their essential columns. Use a clear, simple format.

    ### 3. Core Logic Pseudocode
    Write high-level pseudocode for the main business logic of one of the key modules. This should illustrate the sequence of operations.

    Please ensure the output is well-structured and easy to understand.
    """

    try:
        response = model.generate_content(prompt)
        # The 'to_markdown' function in the new Gemini library helps format the output nicely
        return response.text
    except Exception as e:
        print(f"[ERROR] Failed to generate content from Google Gemini: {e}")
        return f"An error occurred while communicating with the AI. Details: {e}"


@app.route('/', methods=['GET', 'POST'])
def index():
    """Main route for the web application."""
    output = ""
    if request.method == 'POST':
        requirement = request.form['requirement']
        if requirement:
            output = generate_technical_specs(requirement)
    return render_template('index.html', output=output)


if __name__ == '__main__':
    # Runs the Flask app on a local server
    app.run(debug=True)