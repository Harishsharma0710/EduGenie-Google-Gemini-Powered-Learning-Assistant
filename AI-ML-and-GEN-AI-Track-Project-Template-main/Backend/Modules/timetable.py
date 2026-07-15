from models.gemini_model import get_gemini_response

def build_timetable(text: str) -> str:
    prompt = f"""
    You are a master productivity coach. Create a structured weekly timetable based on the user's goals and availability.
    
    CRITICAL FORMATTING RULES:
    1. Structure your response into exactly three sections:
       ### Weekly Overview
       ### Day-by-Day Schedule
       ### Productivity Tips
    2. Do not use any introductory text. Start directly with '### Weekly Overview'.
    
    User Input: "{text}"
    """
    return get_gemini_response(prompt, temperature=0.5)
