from services.weather_api import get_weather
from services.data_processor import process_raw_data

print(process_raw_data(get_weather("Moscow")))