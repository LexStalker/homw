from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio


api = '7855279448:AAEkYcgwlZiuuGYsvBmM1YFGwwmXcBfigtE'
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())
kb = ReplyKeyboardMarkup()
button = KeyboardButton(text = 'Info')
button1 = KeyboardButton(text= 'Buy')
kb.add(button1)
kb.add(button)
# kb.row kb.insert
@dp.message_handler(commands= ['start'])
async def start(message):
    await message.answer('Hello', reply_markup = kb)

@dp.message_handler(text = 'Info')
async def inform(message):
    await message.answer('Info bot')

# @dp.message_handler(text = ['MMS'])
# async def mms_message(message):
#     print('mms message ')
#     await message.answer('mms message!')
#
# @dp.message_handler(commands=['Start'])
# async def start_message(message):
#     print('start message')
#     await message.answer('Hello ')
#
# @dp.message_handler()
# async def all_message(message):
#     print('SMS')
#     await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

