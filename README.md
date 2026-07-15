# EduGenie 🧞‍♂️

EduGenie is an AI-powered educational assistant that helps students learn faster and more effectively. It uses the Gemini API to generate concise summaries, interactive flashcards, and test quizzes from any topic you provide.

## Features

- **📝 Notes Summary:** Instantly generate clear, structured summaries of complex topics.
- **📇 Flashcards:** Automatically create interactive, flippable flashcards to memorize key concepts.
- **🎯 Test & Quiz:** Generate multiple-choice quizzes to test your knowledge and see explanations for the correct answers.
- **💾 Export & Save:** Copy or download your generated study materials as text files for offline use.

## Tech Stack

- **Frontend:** HTML, Tailwind CSS, Vanilla JavaScript, FontAwesome (Icons), Marked.js (Markdown parsing)
- **Backend:** Python, FastAPI, Uvicorn
- **AI Model:** Google Gemini API (`gemini-2.5-flash`)

## Folder Structure

```text
EDUGENIE/
│
├── frontend/             # User Interface (Static Files)
│   ├── index.html        # Main HTML layout
│   └── script.js         # Frontend logic and API calls
│
├── backend/              # API Server
│   ├── main.py           # FastAPI application setup
│   ├── requirements.txt  # Python dependencies
│   ├── .env.example      # Environment variables template
│   │
│   ├── models/           # AI Model Configuration
│   │   └── gemini_model.py
│   │
│   └── modules/          # Feature Processors
│       ├── summary.py
│       ├── flashcards.py
│       └── test_quiz.py
│
└── README.md             # Project documentation

How to Run Locally
1. Backend Setup
Open a terminal and navigate to the backend folder:
code
Bash
cd backend
Install the required Python packages:
code
Bash
pip install -r requirements.txt
Create a .env file in the backend folder and add your Gemini API key:
code
Env
GEMINI_API_KEY="your_api_key_here"
Start the FastAPI server:
code
Bash
uvicorn main:app --reload
The backend will run at http://127.0.0.1:8000.
