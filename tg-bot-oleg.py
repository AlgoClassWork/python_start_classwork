# Импортируем нужные нам функции из библиотеки телеграм
from random import shuffle
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

menu = ReplyKeyboardMarkup ([
    [KeyboardButton('Привет 😀'), KeyboardButton('Как дела? 😴')],
    [KeyboardButton('Шутка 💀'), KeyboardButton('Посоветуй фильм 💯')],
    [KeyboardButton('Мем 👽')]

], resize_keyboard=True)

jokes = ['Колобок повесился', 'Русалка села шпагат', 'Рыба утонула']

meme_url = ['https://avatars.mds.yandex.net/i?id=c79301499be578b27f389bc921733542_l-10289644-images-thumbs&n=13',
            'https://avatars.mds.yandex.net/i?id=5bae6c294e9c9a3c1b97bddc8a89d3c093420b23-3937533-images-thumbs&n=13',
            'https://images.steamusercontent.com/ugc/2053118509456565596/FDAC81B4F62A7BC79CB914DEA27C1815EA3DE698/'
            ]

quiz_question = 'Какого цвета чернокожие?'
quiz_answers = [
    InlineKeyboardButton('Черные', callback_data='right'),
    InlineKeyboardButton('Зеленые', callback_data='wrong'),
]

# Реакция на команду /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # update - информация о входящем сообщении
    # context - информация о пользовательских данных
    # reply_text - отправить ответ пользователю
    await update.message.reply_text('Здравствуйте меня зовут Олег! /help',
                                    reply_markup=menu)

# Реакция на команду /help
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # update - информация о входящем сообщении
    # context - информация о пользовательских данных
    # reply_text - отправить ответ пользователю
    await update.message.reply_text('Я умею шутить шутки и рекомендовать фильмы')

# Реакция на любое текстовое сообщение пользователя
async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Получаем текст сообщения пользователя
    text = update.message.text.lower()
    if 'привет' in text:
        await update.message.reply_text('Вечер в хату!')
    elif 'как дела' in text:
        await update.message.reply_text('Отлично как у вас?')

    elif 'мем' in text:
        shuffle(meme_url)
        await update.message.reply_photo(photo=meme_url[0], caption='ахахахах')

    elif 'шутка' in text:
        shuffle(jokes)
        await update.message.reply_text( jokes[0] )

    elif 'викторина' in text:
        answer_buttons = InlineKeyboardMarkup.from_row(quiz_answers)
        await update.message.reply_text(quiz_question, reply_markup=answer_buttons)

    elif 'фильм' in text:
        await update.message.reply_text('Какой жанр вас интересует?')
        context.user_data['ожидание жанра'] = True
    elif context.user_data.get('ожидание жанра'):
        context.user_data['ожидание жанра'] = False
        if 'боевик' in text:
            await update.message.reply_text('https://www.kinopoisk.ru/film/666/?utm_referrer=yandex.ru')
        elif 'комедия' in text:
            await update.message.reply_text('Один дома')
        else:
            await update.message.reply_text('Таких жанров я не знаю')
    else:
        await update.message.reply_text('Извините я вас не понимаю')

# ТОКЕН - позволяет соеденить вашего бота и код
TOKEN = '7962898757:AAEqwj-9f2sYh0u7_ar7XDUoDFjcVI99kOs'
# Создаем наше телеграм приложение
app = Application.builder().token(TOKEN).build()
# Отслеживание событий
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))
# Запуск приложения
print('Запуск бота . . .')
app.run_polling()
