#переписать коннектор под импорт в main и вызов его с параметрами из .env

import asyncio
import asyncpg
from dotenv import load_dotenv
import os

load_dotenv()
class Database:
    def __init__(self):
        self.pool = None
        self.TTL_HOURS = 4

    async def create_pool(self):
        self.pool = await asyncpg.create_pool(
            user = os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            min_size= 5,
            max_size= 20,
            
        )
        return self

    async def close_pool(self):
        if self.pool:
            await self.pool.close()
   
    async def get_pool(self):
        if not self.pool:
            raise RuntimeError("База данных не соединена. Создайте соединение")
        return self.pool