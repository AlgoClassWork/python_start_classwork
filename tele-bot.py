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
        await update.message.reply_text('Привет чува(к-иха)')
    elif 'как дела' in text:
        await update.message.reply_text('Нормально как у тебя?')
    elif 'норм' in text:
        await update.message.reply_text('Я тебя поздравляю')
    elif 'фильм' in text:
        await update.message.reply_text('Какой жанр?')
        context.user_data['awaiting_genre'] = True
    elif context.user_data.get('awaiting_genre'):
        genre = text
        if 'комедия' in genre:
            await update.message.reply_text('Мальчишник в вегасе')
        elif 'ужас' in genre:
            await update.message.reply_text('Пила')
        context.user_data.pop('awaiting_genre')
    else:
        await update.message.reply_text('Извини я тебя не понимаю')

def main():
    application = Application.builder().token("7180974589:AAEWa3rIqZc3i8WeBjwhGxOPY5JV4Mf3jdE").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

main()
