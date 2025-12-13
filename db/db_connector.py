import asyncio
import asyncpg
from dotenv import load_dotenv
import os

load_dotenv()

async def run():
    try:
        conn = await asyncpg.connect(
            user = os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
        )
        await conn.execute("""
            CREATE TABLE users(
                id serial PRIMARY KEY,
                name text,
                dob date               
            )
        """)

    finally:
        await conn.close()
asyncio.run(run())