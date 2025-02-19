# pip install python-telegram-bot
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# обработка команды старт
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Привет! Я Чад, как поживаешь? \n'
        'Отправь /help чтобы получить справку'
    )

# обработка команды хелп
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Могу пообщаться с тобой \n'
        'Могу пошутить \n'
        'Могу порекомендовать фильм'
    )

# обработка сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()  # получаем текст сообщения
    if text == 'привет':
        await update.message.reply_text('Здравствуй, дядя!')
    elif text == 'как дела':
        await update.message.reply_text('Не важно, как твои?')
    elif text == 'хорошо':
        await update.message.reply_text('Рад слышать')
    elif text == 'шутка':
        await update.message.reply_text('Колобок повесился')
    elif 'фильм' in text:
        await update.message.reply_text('Какой жанр?')
        context.user_data['жанр'] = True
    elif context.user_data.get('жанр'):
        if 'боевик' in text:
            await update.message.reply_text('https://www.kinopoisk.ru/film/440616/')
        elif 'комедия' in text:
            await update.message.reply_text('https://www.kinopoisk.ru/film/5309059/')
        context.user_data.pop('жанр')
    elif 'картинка' in text:
        # Отправляем картинку по URL
        image_url = 'https://www.ferra.ru/imgs/2024/05/08/05/6460496/c2150453d059e8999c5f0b211ce334f7c869147c.jpg'  # Замените на ваш URL картинки
        await update.message.reply_photo(photo=image_url)

# соединение бота с кодом
app = Application.builder().token('Ваш токен').build()

# подписки на команды
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# запуск
app.run_polling()
