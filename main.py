from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.types import FSInputFile
from aiogram.filters import CommandStart, Command
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode


from parsing import get_source_html, get_items_urls, get_url
from img_path import get_img

from misc import config

# todo: Создание бота
bot = Bot(config.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


# todo: Создание клавиатур
def get_keyboard_start():
    buttons = [
        [types.InlineKeyboardButton(text='Получить статистику игрока', callback_data='season')],
        [types.InlineKeyboardButton(text='Какой ты сегодня агент', callback_data='mood')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_keyboard_stats():
    buttons = [
        [types.InlineKeyboardButton(text='Получить статистику другого игрока', callback_data='season')],
        [types.InlineKeyboardButton(text='Какой ты сегодня агент', callback_data='mood')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_keyboard_mood():
    buttons = [
        [types.InlineKeyboardButton(text='Получить статистику игрока', callback_data='season')],
        [types.InlineKeyboardButton(text='Это не я, давай еще раз!!', callback_data='mood')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_keyboard_season():
    buttons = [
        [types.InlineKeyboardButton(text='За все сезоны', callback_data='stats_all')],
        [types.InlineKeyboardButton(text='Только за нынешний сезон', callback_data='stats')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


# todo: Функции
def make_img_path():
    img_info = get_img()
    img_path = FSInputFile(r".\Mood\\" + img_info[0])
    return img_path, img_info[1]


# todo:  Хэндлеры
@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text='Привет, будущая киберкотлета😎.'
                              ' Если ты хочешь узнать основную информацию о каком-либо игроке, то я тебе с этим помогу!',
                         reply_markup=get_keyboard_start())


@dp.message(Command('mood'))
async def handle_mood(message: types.Message):
    await message.answer_photo(*make_img_path(), reply_markup=get_keyboard_mood())


@dp.message(Command('season'))
async def handle_season(message: types.Message):
    await message.answer('Вам нужна статистика за все сезоны или только за нынешний?',
                         reply_markup=get_keyboard_season())


@dp.message()
async def get_stats_command(message: types.Message):
    nickname = message.text
    if nickname[0] == '!' and '#' in nickname:
        try:
            msg = ('Итак, вот какую информацию нам удалось собрать на этого игрока. '
                   'Но помни, что валорант - командная игра, и опираться только на статистику не стоит!!🤡\n\n')
            url = get_url(nickname[1:], ss)
            get_source_html(url)
            for key, value in get_items_urls(r'source_page.html').items():
                msg += f'<b>{key}</b>: <em>{value}</em>\n\n'
            await message.answer(text=msg, reply_markup=get_keyboard_stats())
        except AttributeError:
            await message.answer(text='Пользователь с таким ником не найден, проверьте написание!')
    else:
        await message.answer(text='Неверно введено имя пользователя, попробуй еще раз!')


# todo: Колбэки
@dp.callback_query(F.data == 'season')
async def callback_season(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Вам нужна статистика за все сезоны или только за нынешний?',
                                  reply_markup=get_keyboard_season())


@dp.callback_query(F.data == 'stats')
async def callback_stats(callback: types.CallbackQuery):
    global ss
    ss = ''
    await callback.answer()
    await callback.message.answer(text='Введите ник игрока, начиная с ! например: !ValenOK#top')


@dp.callback_query(F.data == 'stats_all')
async def callback_stats_all(callback: types.CallbackQuery):
    global ss
    ss = '?season=all'
    await callback.answer()
    await callback.message.answer(text='Введите ник игрока, начиная с ! например: !ValenOK#top')


@dp.callback_query(F.data == 'mood')
async def callback_mood(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(*make_img_path(), reply_markup=get_keyboard_mood())


# todo: функция запуска бота

async def start_bot():
    await dp.start_polling(bot)
