from models.gemini_model import get_gemini_response

def generate_test_quiz(text: str) -> str:
    prompt = f"""
    You are an expert educator. Analyze the following topic and generate a challenging, thought-provoking 10-question Multiple Choice Quiz to test active recall.
    
    CRITICAL INSTRUCTIONS:
    You MUST return ONLY a valid JSON object. Do not include markdown formatting or backticks around the JSON.
    
    Format:
    {{
        "title": "Quiz Title",
        "questions": [
            {{
                "question": "Question text here?",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "correct_index": 0,
                "explanation": "Why this is correct."
            }}
        ]
    }}
    
    Topic: "{text}"
    """
    return get_gemini_response(prompt, temperature=0.4, is_json=True)
