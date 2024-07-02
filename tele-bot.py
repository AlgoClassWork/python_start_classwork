from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Здравствуй человек я сверх продвинутый исскуственный ынтылект \n'
        'Давай пообщаемся на различные высоко ынтелектуальные темы'
    )
  
def main():
    application = Application.builder().token("СЮДА ВСТАВЬТЕ ВАШ ТОКЕН").build()

    application.add_handler(CommandHandler("start", start))
    #application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

main()
