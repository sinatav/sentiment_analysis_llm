from langchain_deepseek import ChatDeepSeek
from src.config import DEEPSEEK_API_KEY

def get_llm():
    if not DEEPSEEK_API_KEY:
        raise ValueError("DeepSeek API key not found. Set it in .env file.")
    
    return ChatDeepSeek(
        model="deepseek-chat",
        api_key=DEEPSEEK_API_KEY,
        temperature=0.0
    )
