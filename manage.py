import os

import asyncio
from dotenv import load_dotenv

from db.db_connector import Database
from db.crud import DatabaseManager

from services.data_processor import process_weather
from bot.app import TelegramBot

load_dotenv()

async def main():
    db = Database()
    await db.create_pool(
        os.getenv("DB_USER"),
        os.getenv("DB_PASSWORD"),
        os.getenv("DB_NAME"),
        os.getenv("DB_HOST"),
        os.getenv("DB_PORT"),
    )
    #manager = DatabaseManager(db)

   # await manager.create_table()
    api_weather = os.getenv('WEATHER_API_KEY')
    
    bot = TelegramBot(os.getenv("TELEGRAM_BOT_TOKEN"),api_weather)
    await bot.start()

    #save bot respone
    #check cache requests
    #get_cache respone
    print("Бот запущен")

   # await db.close_pool()

if __name__ == "__main__":
    asyncio.run(main())