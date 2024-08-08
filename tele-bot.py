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

# соединение telegram бота с кодом
app = Application.builder().token("ВАШ ТОКЕН").build()
# подписки на команды
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
# запуск бота
app.run_polling()


#pip install python-telegram-bot
