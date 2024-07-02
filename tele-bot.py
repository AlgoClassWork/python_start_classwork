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
    elif 'аним' in text:
         await update.message.reply_text('Введите жанр:')
         context.user_data['awaiting_genre'] = True
    elif context.user_data.get('awaiting_genre'):
        genre = text
        if genre == 'приключение':
            await update.message.reply_text('Ван пис')
        elif genre == 'экшен':
            await update.message.reply_text('Атака титаника')
        else:
            await update.message.reply_text('Таких жанров я пока не знаю')
        context.user_data.pop('awaiting_genre')
        

def main():
    application = Application.builder().token("7148594036:AAG-hcT4eLgSjaR1EFVeRUKyonhomaR-C5A").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()


main()
