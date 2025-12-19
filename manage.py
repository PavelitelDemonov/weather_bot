from db.db_connector import Database
from db.crud import DatabaseManager
import asyncio
from services.data_processor import process_raw_data
from services.weather_api import get_weather
from bot.app import TelegramBot

async def main():
    db = Database()
    await db.create_pool()
    
    api_key = os.getenv('WEATHER_API_KEY')
    manager = DatabaseManager(db)

    await manager.create_table()
    
    bot = TelegramBot()

    #save bot respone
    #check cache requests
    #get_cache respone


    await db.close_pool()

if __name__ == "__main__":
    asyncio.run(main())