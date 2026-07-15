import os
import google.generativeai as genai
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def get_gemini_response(prompt: str, temperature: float = 0.3, is_json: bool = False) -> str:
    """Centralized function to call Gemini using the advanced 2.5-flash model."""
    try:
        # Upgraded to a faster, more intelligent model version
        model = genai.GenerativeModel("gemini-2.5-flash")
        
        config = genai.GenerationConfig(temperature=temperature)
        if is_json:
            config.response_mime_type = "application/json"
            
        response = model.generate_content(prompt, generation_config=config)
        return response.text.strip()
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gemini API Error: {str(e)}")
