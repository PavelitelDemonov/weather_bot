from aiogram.types import InlineKeyboardButton, KeyboardButton, Message, ReplyKeyboardRemove
from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode

router = Router()


@router.message(CommandStart())
async def send_welcome(message: Message) -> None:
    await message.answer("Привет!, я бот для отображения прогноза погоды, выбери город",reply_markup=ReplyKeyboardRemove)

@router.message(Command("weather"))
async def cmd_weather(message: Message, weather_service):
    """Обработчик /weather - получаем сервис через DI"""
    # Получаем город из сообщения
    city = message.text.replace('/weather', '').strip()
    if not city:
        city = "Москва"
    
    # Используем сервис погоды
    weather_data = await weather_service.get_weather(city)
    
    # Отправляем ответ
    await message.answer(
        str(weather_data),
        parse_mode=ParseMode.HTML
    )

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "Доступные команды:\n"
        "/start - начать работу\n"
        "/weather <город> - погода\n"
        "/help - помощь"
    )

# Обработчик обычных текстовых сообщений
@router.message(F.text)
async def handle_text(message: Message, weather_service):
    """Если просто написали название города"""
    city = message.text.strip()
    weather_data = await weather_service.get_weather(city)
    await message.answer(str(weather_data))