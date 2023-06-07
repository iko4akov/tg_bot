from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6052813762:AAGiqkpVcYDHlZp7fSpgkirSRJklr1lORdg'


bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("\n--->Сашка дурачек<-----\n")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('САНЯ ТЫ ДАЛБОЕБ!!!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

