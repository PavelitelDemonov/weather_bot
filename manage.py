from db.db_connector import Database
from db.crud import DatabaseManager
import asyncio

async def main():
    db = Database()
    await db.create_pool()

    manager = DatabaseManager(db)

    await manager.create_table()

    #save bot respone
    #check cache requests
    #get_cache respone


    await db.close_pool()

if __name__ == "__main__":
    asyncio.run(main())