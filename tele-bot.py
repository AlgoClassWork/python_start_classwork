from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from random import randint


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Здравствуйте меня зовут бот Генадий. \n'
        'Вот что я умею делать: \n'
        '- Шутить \n'
        '- Рекомендация оняме  \n'
        '- Сыграть во что нибудь \n'
        '- Могу продать вам хлам \n'
        '\n'
        'Что бы вы хотели? \n'
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    text = update.message.text.lower()

    if 'шут' in text:
         await update.message.reply_text('Колобок повесился')


def main():
    application = Application.builder().token("Ваш токен").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()


main()
