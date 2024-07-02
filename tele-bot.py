from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Здравствуй человек я сверх продвинутый исскуственный ынтылект \n'
        'Давай пообщаемся на различные высоко ынтелектуальные темы'
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if 'привет' in text:
        await update.message.reply_text('ты красавчик')
  
def main():
    application = Application.builder().token("ВАШ ТОКЕН").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

main()
