#pip install python-telegram-bot
#7973499836:AAHO_7zjhi4LNDXDxLcbW9_ukDVzbQxQJ9s
from telegram import Update
from telegram.ext import Application, CommandHandler,MessageHandler, filters, ContextTypes



app = Application.builder().token('ВАШ ТОКЕН').build()

app.run_polling()
