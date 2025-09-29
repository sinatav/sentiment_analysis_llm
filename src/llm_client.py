from langchain_community.llms import DeepSeek
from src.config import DEEPSEEK_API_KEY

def get_llm():
    if not DEEPSEEK_API_KEY:
        raise ValueError("DeepSeek API key not found. Set it in .env file.")
    
    return DeepSeek(
        model="gpt-40-mini",
        api_key=DEEPSEEK_API_KEY,
        temperature=0.0
    )