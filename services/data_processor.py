import json
from dataclasses import dataclass,asdict
from typing import Dict,Any,Optional
from datetime import datetime

@dataclass
class WeatherData:
    city_name: str
    main: str
    description: str
    temperature: float
    feels_like: float
    pressure: int
    humidity: int
    visibility: int
    wind_speed: float
    
    def __str__(self):
        return(f"""
                🌤️ Погода: {self.main} ({self.description})
                🌡️ Температура: {self.temperature}°C (ощущается как {self.feels_like}°C)
                💨 Ветер: {self.wind_speed} м/с
                💧 Влажность: {self.humidity}%
                📊 Давление: {self.pressure} гПа
                👁️ Видимость: {self.visibility} м
                    Город: {self.city_name}
            """)

def process_raw_data(raw_data):
        try:
            weather_data = json.loads(raw_data)
            weather_class = WeatherData(
                main = weather_data['weather'][0]["main"] ,
                description = weather_data['weather'][0]["description"],
                temperature = round(weather_data['main']['temp']),
                feels_like = round(weather_data['main']['feels_like']),
                pressure = weather_data['main']["pressure"],
                humidity = weather_data['main']["humidity"],
                visibility = weather_data['visibility'],
                wind_speed = weather_data['wind']["speed"],
                city_name = weather_data["name"],
            )
            return weather_class
        except (KeyError, IndexError, TypeError) as e:
              return f"Ошибка обработки данных {e}"