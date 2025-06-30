# Импортируем нужные классы и функции из библиотеки telegram
from telegram import (
    Update,                     # Содержит входящее сообщение/команду от пользователя
    ReplyKeyboardMarkup,        # Для создания обычных кнопок (внизу чата)
    KeyboardButton,             # Каждая отдельная кнопка
    InlineKeyboardMarkup,       # Для создания кнопок внутри сообщения (inline)
    InlineKeyboardButton,       # Каждая отдельная inline-кнопка
    InputMediaPhoto             # Для отправки фото с подписями
)

# Импорт из telegram.ext — расширения для логики и управления ботом
from telegram.ext import (
    Application,                # Основной класс, запускающий бота
    CommandHandler,             # Обработчик команд, например: /start
    MessageHandler,             # Обработчик обычных сообщений
    CallbackQueryHandler,       # Обработчик нажатий на inline-кнопки
    filters,                    # Набор фильтров (например, текст без команд)
    ContextTypes                # Тип контекста — сюда можно сохранять user_data
)

# Импорт стандартных функций
from random import shuffle, randint  # Для случайных шуток и случайных чисел

# === ГЛАВНОЕ МЕНЮ С КНОПКАМИ ===
# ReplyKeyboardMarkup — создаёт кнопки внизу чата
main_menu = ReplyKeyboardMarkup([
    [KeyboardButton("👋 Привет"), KeyboardButton("😂 Шутка")],
    [KeyboardButton("🎬 Фильмы"), KeyboardButton("🎮 Игра")],
    [KeyboardButton("📊 Викторина"), KeyboardButton("📷 Мем")],
    [KeyboardButton("🤔 Как дела?"), KeyboardButton("🙋 Что делаешь?")],
    [KeyboardButton("👋 Пока")]
], resize_keyboard=True)  # resize_keyboard=True делает кнопки компактнее

# Шутки для выбора
jokes = ['Колобок повесился 😂', 'Русалка села на шпагат 🧜‍♀️', 'Рыба утонула 🐟💦']

# Ссылка на мем-картинку
meme_url = "https://i.imgur.com/OuKDd6T.jpeg"  # Можно заменить на любой другой URL с изображением

# Данные для викторины
quiz_question = "Сколько будет 2 + 2?"  # Текст вопроса
quiz_answers = [  # Inline кнопки-ответы
    InlineKeyboardButton("4 ✅", callback_data="quiz_right"),
    InlineKeyboardButton("5 ❌", callback_data="quiz_wrong"),
    InlineKeyboardButton("22 🤡", callback_data="quiz_wrong")
]

# === ОБРАБОТЧИК КОМАНДЫ /start ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Отправляем приветственное сообщение с главными кнопками
    await update.message.reply_text(
        "Здарова, я веселый бот ОЛЕГ 🤖\nЖми кнопки, пиши что хочешь!",
        reply_markup=main_menu
    )
    # Сохраняем в user_data счётчик побед в игре, если он ещё не установлен
    context.user_data.setdefault("wins", 0)

# === ГЛАВНЫЙ ОБРАБОТЧИК ВСЕХ СООБЩЕНИЙ ===
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    request = update.message.text.lower()  # Приводим текст к нижнему регистру

    # Приветствие
    if "привет" in request:
        await update.message.reply_text("Вечер в хату! 🧢")

    # Ответ на "как дела"
    elif "как дела" in request:
        await update.message.reply_text("У меня всё по кайфу! А у тебя? 🔥")

    # Ответ на "что делаешь"
    elif "что делаешь" in request:
        await update.message.reply_text("Да ниче, просто живу, как и ты 🧘")

    # Случайная шутка
    elif "шутка" in request:
        shuffle(jokes)  # Перемешиваем шутки
        await update.message.reply_text(jokes[0])  # Отправляем первую из перемешанного списка

    # Кнопки выбора жанра фильма
    elif "фильмы" in request:
        genre_menu = ReplyKeyboardMarkup([
            [KeyboardButton("🧨 Боевик"), KeyboardButton("🤣 Комедия")],
            [KeyboardButton("👻 Ужасы"), KeyboardButton("🔙 Назад")]
        ], resize_keyboard=True)
        context.user_data["waiting_for_genre"] = True  # Устанавливаем флаг "ждём жанр"
        await update.message.reply_text("Выбери жанр фильма 🎞️:", reply_markup=genre_menu)

    # Ответ на жанр фильма
    elif context.user_data.get("waiting_for_genre"):
        context.user_data["waiting_for_genre"] = False  # Снимаем флаг
        if "боевик" in request:
            await update.message.reply_text("Атака титаника 💥")
        elif "комедия" in request:
            await update.message.reply_text("Один дома 🤪")
        elif "ужас" in request:
            await update.message.reply_text("Пила 🪚")
        else:
            await update.message.reply_text("Чёт не понял жанр 🤷")
        # Возвращаем основное меню
        await update.message.reply_text("Возвращаюсь в главное меню 🔄", reply_markup=main_menu)

    # Игра "Угадай число"
    elif "игра" in request:
        num = randint(1, 100)  # Загадываем случайное число
        context.user_data["game_number"] = num  # Сохраняем число в user_data
        context.user_data["game_tries"] = 5     # Сохраняем кол-во попыток
        await update.message.reply_text("🎯 Угадай число от 1 до 100. У тебя 5 попыток!")

    # Проверка числа во время игры
    elif "game_number" in context.user_data:
        try:
            guess = int(request)  # Пробуем преобразовать ввод в число
        except ValueError:
            await update.message.reply_text("🤓 Это не число. Попробуй нормально.")
            return

        context.user_data["game_tries"] -= 1
        num = context.user_data["game_number"]

        if guess == num:
            context.user_data["wins"] += 1  # Увеличиваем счётчик побед
            await update.message.reply_text(f"🎉 Красавчик! Ты угадал! Побед: {context.user_data['wins']}")
            context.user_data.pop("game_number")  # Убираем число — игра закончена
        elif context.user_data["game_tries"] == 0:
            await update.message.reply_text(f"💀 Проиграл. Было число: {num}")
            context.user_data.pop("game_number")
        else:
            # Подсказка — больше или меньше
            hint = "📉 Меньше" if guess > num else "📈 Больше"
            await update.message.reply_text(f"{hint}. Осталось попыток: {context.user_data['game_tries']}")

    # Начать викторину
    elif "викторина" in request:
        markup = InlineKeyboardMarkup.from_row(quiz_answers)  # Создаём inline-кнопки
        await update.message.reply_text(quiz_question, reply_markup=markup)

    # Мем-картинка
    elif "мем" in request:
        await update.message.reply_photo(photo=meme_url, caption="Лови мем! 😹")

    # Прощание
    elif "пока" in request:
        await update.message.reply_text("Бывай, брат! Возвращайся 🔥", reply_markup=main_menu)

    # Назад в главное меню
    elif "назад" in request:
        await update.message.reply_text("🔙 Назад в меню", reply_markup=main_menu)

    # Если бот ничего не понял
    else:
        await update.message.reply_text("❓ Не понял. Жми кнопки внизу ⬇️")

# === ОБРАБОТКА КНОПОК ВИКТОРИНЫ ===
async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query  # Получаем объект запроса (нажатие кнопки)
    await query.answer()  # Сообщаем Telegram, что обработали нажатие

    if query.data == "quiz_right":
        await query.edit_message_text("✅ Правильно! Ты умный 😎")
    elif query.data == "quiz_wrong":
        await query.edit_message_text("❌ Неправильно! Попробуй в следующий раз 🤓")

# === ЗАПУСК БОТА ===

TOKEN = "YOUR_BOT_TOKEN"  # 👈 ВСТАВЬ СЮДА свой токен от BotFather

app = Application.builder().token(TOKEN).build()  # Создаём приложение

# Обработчики
app.add_handler(CommandHandler("start", start))  # Команда /start
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  # Всё, кроме команд
app.add_handler(CallbackQueryHandler(handle_callback))  # Обработка inline-кнопок

print("Бот ОЛЕГ запущен 💥")  # Лог в терминал
app.run_polling()  # Запускаем опрос сервера Telegram (бесконечный цикл)
