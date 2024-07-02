from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

        
def main():
    application = Application.builder().token("ТВОЙ ТОКЕН").build()

    application.add_handler(CommandHandler("start", start))
    #application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

main()
