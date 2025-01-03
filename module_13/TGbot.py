from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio


api = '7855279448:AAEkYcgwlZiuuGYsvBmM1YFGwwmXcBfigtE'
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

class UserState(StatesGroup):
    adress = State()

@dp.message_handler(text= 'Заказать')
async def buy(message):
    await message.answer('Отправь свой адрес')
    await UserState.adress.set()

@dp.message_handler(state= UserState.adress)
async def fsm_handler(message, state):
    await state.update_data(first = message.text)
    data = await state.get_data()
    await message.answer(f"Доставка будет отправлена на {data['first']}")
    await state.finish()

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

