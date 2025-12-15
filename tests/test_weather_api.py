from services.weather_api import get_weather
import json

weather_data_structure = get_weather('Moscow')
print(weather_data_structure)
