from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6555949003:AAEair6VGgkh9CvBQIvc2WhGV0h9dSEJlkY')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.KeyboardButton('MySneakersShop', web_app=WebAppInfo(url='https://nikitka08.github.io/TestTgbot/')))
    await message.answer('Привет👋 \nЭто MySneakersShopBot👟\n'
                         'В моем веб приложение есть огромное количество кроссовок на твой вкус😉\n'
                         'Начни Your Sneakers Sopping🛍️', reply_markup=markup)

executor.start_polling(dp)
