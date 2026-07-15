'''import torch
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "MBZUAI/LaMini-Flan-T5-783M"
_pipeline_instance = None

def get_lamini_pipeline():
    """Lazy-loads the local model to save memory until it's actually needed."""
    global _pipeline_instance
    if _pipeline_instance is None:
        print("Loading local LaMini model into CPU memory...")
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
        _pipeline_instance = pipeline(
            "text2text-generation",
            model=model,
            tokenizer=tokenizer,
            max_length=512,
            temperature=0.3,
            device="cpu"
        )
    return _pipeline_instance