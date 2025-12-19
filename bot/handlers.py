from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
import asyncio

from services.data_processor import process_weather

router = Router()

@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer(f"Бот для просмотра погоды, введите /city +\"название города\"")

@router.message(Command('city'))
async def cmd_get_city(message: Message, weather_api):
    city = message.text.split(sep=" ")
    city = message.text.split()[1] if len(message.text.split()) > 1 else "Москва"
    weather = await process_weather(city=city, api_key=weather_api)
    weather_str = weather.__str__()
    await message.answer(f"Погода: {weather_str}")