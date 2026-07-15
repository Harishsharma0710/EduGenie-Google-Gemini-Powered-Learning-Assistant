from models.gemini_model import get_gemini_response

def generate_roadmap(text: str, level: str = "Basic") -> str:
    prompt = f"""
    You are a master curriculum designer. Create a comprehensive, step-by-step learning roadmap for mastering the following topic, tailored specifically for a {level} level learner.
    
    CRITICAL FORMATTING RULES:
    1. Structure your response into exactly three sections using these headers:
       ### Phase 1: Foundations
       ### Phase 2: Core Concepts
       ### Phase 3: Applied Mastery
    2. For each phase, include specific, actionable learning steps, recommended project ideas, and estimated completion times suitable for someone starting at the {level} level.
    3. Do not use any introductory text. Start directly with '### Phase 1: Foundations'.
    
    Topic: "{text}"
    Level: "{level}"
    """
    return get_gemini_response(prompt, temperature=0.6)
