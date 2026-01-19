import os
from dotenv import load_dotenv 
from langchain_openai import ChatOpenAI

load_dotenv() 

def get_llm():
    """Returns the primary reasoning model."""
    api_key = os.getenv("OPENAI_API_KEY")
    
    # Debugging check (stops the script early if key is missing)
    if not api_key:
        raise ValueError("❌ FATAL: OPENAI_API_KEY not found in .env file or environment.")

    return ChatOpenAI(
        model="gpt-4o",
        temperature=0, 
        api_key=api_key
    )