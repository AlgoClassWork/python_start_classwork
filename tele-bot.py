from telegram import Update
from telegram.ext import (
Application, CommandHandler,
MessageHandler, filters, ContextTypes)

#обработка команды старт
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'ПРИВЕТ БРООООООООО!!! \n' 
        'Отправь /help чтобы получить справку')
    
#обработка команды help  
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Могу пообщаться с тобой \n'
        'Могу пошутить \n'
        'Могу порекомендовать фильмы \n')

# соединение telegram бота с кодом
app = Application.builder().token("ВАШ ТОКЕН").build()
# подписки на команды
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help)) # new
# запуск бота
app.run_polling()


#pip install python-telegram-bot
