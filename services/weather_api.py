import httpx
from typing import Any, Dict
import json


async def get_weather(city:str,api_key:str) -> Dict[str, Any]:
    try:
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
    
