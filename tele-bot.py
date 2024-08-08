from telegram import Update
from telegram.ext import (
Application, CommandHandler,
MessageHandler, filters, ContextTypes)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('ПРИВЕТ БРООООООООО!!!')

# соединение telegram бота с кодом
app = Application.builder().token("ВАШ ТОКЕН").build()
# подписки на команды
app.add_handler(CommandHandler("start", start))
# запуск бота
app.run_polling()


#pip install python-telegram-bot
