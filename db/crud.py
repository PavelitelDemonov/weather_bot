from db_connector import Database


class DatabaseManager:
    def __init__(self,db:Database):
        self.db = db

    async def create_table(self):
        pool = self.db.get_pool()
        async with pool.acquire() as conn:
            await conn.execute("""
                    CREATE TABLE weather_requests(
                        id serial PRIMARY KEY,
                        cache_key VARCHAR(255) UNIQUE NOT NULL,
                        weather_data JSONB NOT NULL,
                        created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW() 
                    )
                """)
    
    async def save_cache(self, city:str,weather_data: dict):
        pool = self.db.get_pool()
        async with pool.acquire() as conn:
            await conn.execute("""
                INSERT INTO weather_requests (cache_key, weather_data)
                VALUES ($1, $2::jsonb)
                ON CONFLICT (cache_key) 
                DO UPDATE SET 
                    weather_data = EXCLUDED.weather_data,
                    created_at = NOW()
            """, f"weather_{city}", weather_data)
    
    async def get_weather_cache(self, city:str, ttl_hours: int = 1 ):
        pool = self.db.get_pool()
        async with pool.acquire() as conn:
            result = await conn.fetchrow("""
                SELECT weather_data 
                FROM weather_requests
                WHERE cache_key = $1
                AND created_at > NOW() - INTERVAL '$2 hours'
""", f"weather_{city}", ttl_hours)
            return dict(result['weather_data']) if result  else None
    
    async def cleanup_cache(self):
        pool = self.db.get_pool()
        async with pool.acquire() as conn:
            await conn.execute("""
                DELETE FROM weather_cache 
                WHERE created_at < NOW() - INTERVAL '1 hour'
            """)