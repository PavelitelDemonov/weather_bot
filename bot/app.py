from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from .handlers import router

class TelegramBot:
    def __init__(self, token:str, weather_api):
        self.bot = Bot(token=token)
        self.storage = MemoryStorage()
        self.dp = Dispatcher(storage=self.storage)
        self.weather_api = weather_api

        self.dp.include_router(router)
    
        self.dp["weather_api"] = weather_api

    async def start(self):
        await self.dp.start_polling(self.bot)