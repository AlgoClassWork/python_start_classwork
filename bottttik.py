from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from random import choice, shuffle

# Клавиатура с кнопками
menu = ReplyKeyboardMarkup([
    [KeyboardButton('Привет 👋'), KeyboardButton('Как дела? 🙂')],
    [KeyboardButton('Шутка 😂'), KeyboardButton('Рекомендация фильма 🎬')]
], resize_keyboard=True)

# Шутки
jokes = [
    'Колобок повесился 🤯',
    'Русалка села на шпагат 🧜‍♀️',
    'Рыба утонула 🐠💦',
    'Медуза ударила током... и сама испугалась ⚡',
    'Ёжик пошёл бриться 🦔🪒'
]

# Приветствия
greetings = [
    'Привет-привет! 👋',
    'Здравствуй, мой друг! 😊',
    'Салют! Рад тебя видеть 😎'
]

# Ответы на "Как дела?"
how_are_you = [
    'Отлично, как у тебя? 😄',
    'Лучше не бывает! ✨ А у тебя как?',
    'Живу, шучу, общаюсь! 😁'
]

# Рекомендации фильмов по жанрам
movie_recommendations = {
    'боевик': ['Джон Уик 🔫', 'Неудержимые 💥', 'Миссия невыполнима 🎯'],
    'комедия': ['Очень страшное кино 😂', 'Маска 😷', 'Диктатор 👑'],
    'драма': ['Зелёная миля 💚', '1+1 (Неприкасаемые) 👨‍🦽', 'Побег из Шоушенка 🏃‍♂️'],
    'фантастика': ['Интерстеллар 🚀', 'Начало 🌀', 'Матрица 🧠'],
    'ужасы': ['Астрал 👻', 'Пила 🪚', 'Заклятие 😱'],
}

# Команда /start
async def start(update, context):
    await update.message.reply_text('Привет, я бот Олег! Напиши /help чтобы узнать, что я умею 🤖', reply_markup=menu)

# Команда /help
async def help(update, context):
    await update.message.reply_text('Я умею:\n• Приветствовать тебя 👋\n• Шутить 😂\n• Давать советы по фильмам 🎬\nПросто нажми нужную кнопку!')

# Основная логика обработки сообщений
async def check_answer(update, context):
    user_text = update.message.text.lower()

    if 'привет' in user_text:
        await update.message.reply_text(choice(greetings))
    elif 'как дела' in user_text:
        await update.message.reply_text(choice(how_are_you))
    elif 'шутка' in user_text:
        await update.message.reply_text(choice(jokes))
    elif 'рекомендация фильма' in user_text:
        genres = ', '.join(movie_recommendations.keys())
        await update.message.reply_text(f'Какой жанр тебя интересует? 📽️ (доступно: {genres})')
        context.user_data['awaiting_genre'] = True
    elif context.user_data.get('awaiting_genre'):
        genre = user_text.strip()
        context.user_data['awaiting_genre'] = False
        if genre in movie_recommendations:
            film = choice(movie_recommendations[genre])
            await update.message.reply_text(f'Советую посмотреть: {film}')
        else:
            await update.message.reply_text('Упс! Такого жанра нет 😅 Попробуй другой!')
    else:
        await update.message.reply_text('Извини, я тебя не понял 🤔 Попробуй нажать на кнопку ниже!')

# Запуск бота
TOKEN = 'ВАШ ТОКЕН'
app = Application.builder().token(TOKEN).build()

# Обработчики
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_answer))

app.run_polling()
