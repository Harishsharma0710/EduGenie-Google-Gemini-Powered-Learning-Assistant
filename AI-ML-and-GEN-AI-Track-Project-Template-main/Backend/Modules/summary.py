from models.gemini_model import get_gemini_response

def summarize_text(text: str) -> str:
    prompt = f"""
    You are an expert research analyst. Compress the following text into a high-yield executive study summary.
    
    CRITICAL FORMATTING RULES:
    1. Structure your response into exactly three sections using these headers:
       ### Core Objective
       ### Key Learning Pillars
       ### Conclusion
    2. Under 'Key Learning Pillars', use concise bullet points.
    3. Do not use any introductory text. Start directly with '### Core Objective'.
    
    Text: "{text}"
    """
    return get_gemini_response(prompt, temperature=0.3)
