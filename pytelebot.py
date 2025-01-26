#pip install python-telegram-bot
#7973499836:AAHO_7zjhi4LNDXDxLcbW9_ukDVzbQxQJ9s
from telegram import Update
from telegram.ext import Application, CommandHandler,MessageHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text (
        'Привет Я Чад как поживаешь? \n'
        'Отправь /help чтобы получить справку'
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text (
        'Могу пообщаться с тобой \n'
        'Могу пошутить \n'
        'Могу порекомендовать фильм'
    )

app = Application.builder().token('7973499836:AAHO_7zjhi4LNDXDxLcbW9_ukDVzbQxQJ9s').build()

app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help))

app.run_polling()
