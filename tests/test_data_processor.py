from services.weather_api import get_weather
from services.data_processor import process_weather

print(process_weather(get_weather("Moscow")))