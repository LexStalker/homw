from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


api = '7855279448:AAEkYcgwlZiuuGYsvBmM1YFGwwmXcBfigtE'
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

@dp.message_handler(text = ['MMS'])
async def mms_message(message):
    print('mms message ')
    await message.answer('mms message!')

@dp.message_handler(commands=['Start'])
async def start_message(message):
    print('start message')
    await message.answer('Hello ')

@dp.message_handler()
async def all_message(message):
    print('SMS')
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

