#переписать коннектор под импорт в main и вызов его с параметрами из .env

import asyncio
import asyncpg
import os

class Database:
    def __init__(self):
        self.pool = None
        self.TTL_HOURS = 4

    async def create_pool(self, user, password, database, host, port):
        self.pool = await asyncpg.create_pool(
            user = user,
            password=password,
            database=database,
            host=host,
            port=port,
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