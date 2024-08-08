from telegram import Update
from telegram.ext import (
Application, CommandHandler,
MessageHandler, filters, ContextTypes)

# обработка команды старт
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'ПРИВЕТ БРООООООООО!!! \n' 
        'Отправь /help чтобы получить справку')
    
# обработка команды help  
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Могу пообщаться с тобой \n'
        'Могу пошутить \n'
        'Могу порекомендовать фильмы')

# обработка всех сообщений которые отправляет пользователь
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower() # получаем текст сообщения пользователя
    if text == 'привет':
        await update.message.reply_text('Здравствуйте мой господин')
    elif text == 'как дела':
        await update.message.reply_text('Не важно как твои?')
    elif text == 'хорошо':
        await update.message.reply_text('Рад это слышать господин')
    elif text == 'шутка':
        await update.message.reply_text('Колобок повесился')
    elif 'фильм' in text:
        await update.message.reply_text('Какой жанр?')
        context.user_data['жанр'] = True
    elif context.user_data.get('жанр'):
        if 'боевик' in text:
            await update.message.reply_text('https://www.kinopoisk.ru/film/1318972/')
        elif 'комедия' in text:
            await update.message.reply_text('https://www.kinopoisk.ru/film/476/')
        context.user_data.pop('жанр')
    else:
        await update.message.reply_text('Извини я тебя не понимаю')
       

# соединение telegram бота с кодом
app = Application.builder().token("ВАШ ТОКЕН").build()
# подписки на команды
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
# запуск бота
app.run_polling()


#pip install python-telegram-bot
