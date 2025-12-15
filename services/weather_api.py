import httpx
import asyncio
from typing import Any, Dict
from dotenv import load_dotenv
import os
import json

load_dotenv()

async def get_weather(city:str) -> Dict[str, Any]:
    try:
        api_key = os.getenv('WEATHER_API_KEY')
        if not api_key:
            return{"Ошибка": "Не получен api ключ"}
        url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q" : city,
            "appid" : api_key,
            'units' : 'metric',
            'lang' : "ru",
        }
        async with httpx.AsyncClient(timeout=10.0) as client:
            respone = await client.get(url,params=params)
            respone.raise_for_status()
            weather_data = respone.json()
        return json.dumps(weather_data, indent=2)
    except(httpx.HTTPStatusError, httpx.RequestError, json.JSONDecodeError, Exception) as e:
        print(f"Ошибка : {e}")
    
