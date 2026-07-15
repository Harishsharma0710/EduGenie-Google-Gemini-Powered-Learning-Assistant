from models.gemini_model import get_gemini_response

def generate_flashcards(text: str) -> str:
    prompt = f"""
    You are an expert study aid creator. Create a set of 10 high-yield flashcards for the following topic.
    
    CRITICAL INSTRUCTIONS:
    You MUST return ONLY a valid JSON object. Do not include markdown formatting or backticks around the JSON.
    
    Format:
    {{
        "title": "Flashcards Topic",
        "cards": [
            {{
                "front": "Question or concept name",
                "back": "Detailed answer or definition"
            }}
        ]
    }}
    
    Topic: "{text}"
    """
    return get_gemini_response(prompt, temperature=0.5, is_json=True)
