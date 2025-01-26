#pip install python-telegram-bot
#7973499836:AAHO_7zjhi4LNDXDxLcbW9_ukDVzbQxQJ9s
from telegram import Update
from telegram.ext import Application, CommandHandler,MessageHandler, filters, ContextTypes
# обработка команды старт
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text (
        'Привет Я Чад как поживаешь? \n'
        'Отправь /help чтобы получить справку'
    )
# обработка команды хелп
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text (
        'Могу пообщаться с тобой \n'
        'Могу пошутить \n'
        'Могу порекомендовать фильм'
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower() # получаем текст сообщения
    if text == 'привет':
        await update.message.reply_text('Здравствуй дядя!')
    elif text == 'как дела':
        await update.message.reply_text('Не важно как твои?')
    elif text == 'хорошо':
        await update.message.reply_text('Рад слышать')


# соединение бота с кодом
app = Application.builder().token('7973499836:AAHO_7zjhi4LNDXDxLcbW9_ukDVzbQxQJ9s').build()
# подписки на команды
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
# запуск
app.run_polling()
