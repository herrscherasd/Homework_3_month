from aiogram import Bot, Dispatcher, types, executor
import config
from random import randint
bot = Bot(config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start", "go"])
async def start(message:types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}.")
    await message.answer(f"Используйте /gamestart для начала игры.")

@dp.message_handler(commands="gamestart")
async def game(message:types.Message):
    await message.answer("Начнем игру!")
    await message.answer("Введите любое число от 1 до 10.")

@dp.message_handler(regexp=r"^[1-9]|10$")
async def randomizr(message:types.Message):
    integ = randint(1, 10)
    user_int = int(message.text)
    if integ == user_int:
        await message.reply("Поздравляем! Вы угадали!")
        await message.answer(f"Загаданное число: {integ}")
    else:
        await message.reply("Вы проиграли!")
        await message.answer(f"Загаданное число: {integ}")




executor.start_polling(dp)