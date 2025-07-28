from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters

menu = ReplyKeyboardMarkup([
    [KeyboardButton('привет'), KeyboardButton('как дела')]], resize_keyboard=True
)

async def start(update, context):
    await update.message.reply_text('Привет я бот Олег /help', reply_markup=menu)

async def help(update, context):
    await update.message.reply_text('Я могу с тобой пообщаться')

async def check_answer(update, context):
    user_text = update.message.text.lower()
    if 'привет' in user_text:
        await update.message.reply_text('Привет хозяин')
    elif 'как дела' in user_text:
        await update.message.reply_text('Отлично как у вас?')
    else:
        await update.message.reply_text('Извините я вас не понимаю')

# Создание и запуск бота
TOKEN = 'ваш токен'
app = Application.builder().token(TOKEN).build()
# Подписки на события (команд и сообщений)
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_answer))

app.run_polling()
