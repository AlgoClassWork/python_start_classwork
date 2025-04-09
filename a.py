#pip install python-telegram-bot
from telegram import Update 
from telegram.ext import (
    Application, CommandHandler,
    MessageHandler, filters, ContextTypes
)

async def start(user: Update, context: ContextTypes.DEFAULT_TYPE):
    await user.message.reply_text('Я БОТ ГЕНАДИЙ ЧЕМ МОГУ ВАМ ПОМОЧЬ? /help')

async def help(user: Update, context: ContextTypes.DEFAULT_TYPE):
    await user.message.reply_text('Могу порекомендовать тебе фильмы и что нибудь еще')

async def bot_message(user: Update, context: ContextTypes.DEFAULT_TYPE):
    text = user.message.text.lower()
    context.user_data['жанр'] = False
    if 'привет' in text:
        await user.message.reply_text('Привет бро!')
    elif 'как' in text:
        await user.message.reply_text('Отлично как сам?')
    elif 'фильм' in text:
        await user.message.reply_text('Какой жанр вас интересует?')
        context.user_data['жанр'] = True
    elif context.user_data['жанр']:
        if 'боевик' in text:
            await user.message.reply_text('https://www.kinopoisk.ru/film/41519/')
        elif 'комедия' in text:
             await user.message.reply_text('https://www.kinopoisk.ru/film/361/')
        context.user_data['жанр'] = False
    else:
        await user.message.reply_text('Ищвини я тебя не понимаю')

app = Application.builder().token('Ваш токен').build()

app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help))
app.add_handler(MessageHandler(filters.TEXT, bot_message))

app.run_polling()
