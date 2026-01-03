import os
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'APIs.env')
print(f'Script location: {__file__}')
print(f'Env path: {env_path}')
print(f'File exists: {os.path.exists(env_path)}')

load_dotenv(env_path)

openai_key = os.getenv("OPENAI_API_KEY")
gemini_key = os.getenv("GEMINI_API_KEY")
news_key = os.getenv("NEWS_API_KEY")
weather_key = os.getenv("WEATHER_API_KEY")

print(f"\nOpenAI key loaded: {bool(openai_key)}")
print(f"Gemini key loaded: {bool(gemini_key)}")
print(f"News key loaded: {bool(news_key)}")
print(f"Weather key loaded: {bool(weather_key)}")
