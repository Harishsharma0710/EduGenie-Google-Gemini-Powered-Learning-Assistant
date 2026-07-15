from models.gemini_model import get_gemini_response

def explain_topic(topic: str) -> str:
    prompt = f"""
    You are an expert at breaking down complex concepts for beginners using the Feynman Technique.
    Provide a highly engaging, beginner-friendly educational explanation for: {topic}.
    
    CRITICAL FORMATTING RULES:
    1. Structure your response into exactly three sections using these headers:
       ### Simple Analogy
       ### How it Works (The Core Mechanics)
       ### Real World Use
    2. Do not use any introductory text or filler. Start directly with '### Simple Analogy'.
    3. Use formatting like bold text and bullet points to make the explanation highly readable.
    """
    return get_gemini_response(prompt=prompt, temperature=0.3)
