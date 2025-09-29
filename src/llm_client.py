from langchain.chat_models import ChatOpenAI
from src.config import OPENROUTER_API_KEY

def get_llm():
    if not OPENROUTER_API_KEY:
        raise ValueError("OpenRouter API key not found. Set it in .env file.")
    
    return ChatOpenAI(
        openai_api_base="https://openrouter.ai/api/v1",
        openai_api_key=OPENROUTER_API_KEY,
        model_name="gpt-4o-mini",  # you can also use "gpt-4o" or other models
        temperature=0.0
    )