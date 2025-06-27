# Импортируем нужные нам функции из библиотеки телеграм
from random import shuffle
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Реакция на команду /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # update - информация о входящем сообщении
    # context - информация о пользовательских данных
    # reply_text - отправить ответ пользователю
    await update.message.reply_text('Здравствуйте меня зовут Олег! /help')

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
    elif 'шутка' in text:
        jokes = ['Колобок повесился', 'Русалка села шпагат', 'Рыба утонула']
        shuffle(jokes)
        await update.message.reply_text( jokes[0] )
    elif 'фильм' in text:
        await update.message.reply_text('Какой жанр вас интересует?')
        context.user_data['ожидание жанра'] = True
    elif context.user_data.get('ожидание жанра'):
        context.user_data['ожидание жанра'] = False
        if 'боевик' in text:
            await update.message.reply_text('Форсаж')
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
