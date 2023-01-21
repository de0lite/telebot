from aiogram import Bot, Dispatcher, executor, types
#from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from aiogram.types import chat

API_TOKEN = '5848794310:AAH7xczokZhpiKsHpUesTn-QrfOI-b052lo'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


#@dp.message_handler(commands=['start'])
#async def send_welcome(message: types.Message):
#    await message.reply("Привет!\nЯ Эхо-бот от Артема!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.")

@dp.message_handler(commands=["start"])
def start(message: types.Message):
        bot.send_message(chat.id, 'Я на связи. Напиши мне Привет )')




@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
