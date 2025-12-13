import httpx
from typing import Any, Dict
from dotenv import load_dotenv
import os

load_dotenv()

def get_weather(city:str) -> Dict[str, Any]:
    try:
        api_key = os.getenv('WEATHER_API_KEY')
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    finally:
        respone = httpx.get(url)
    return respone.json()

