from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
from random import choice, randint

# 🤖 Список смешных фраз, которые может отправить бот (по команде "Шутка")
jokes = [
    "Колобок повесился 😂", "Русалка села на шпагат 🧜‍♀️", "Рыба утонула 🐟",
    "Грабитель вернул кошелёк, когда узнал баланс 💸", "Слон сел на Wi-Fi 🐘📶",
    "Программист пошёл на свидание — сделал rollback 🫣", "В носках дырки от пользователей 😅",
    "Когда упал интернет — я снова увидел свою семью 👨‍👩‍👧‍👦", "Я не ленивая, я в энергосберегающем режиме 🔋",
    "Почему кофе не отвечает? Потому что он молчит... ☕😶"
]

# 🖼 Список мемов — каждый мем содержит ссылку на картинку и подпись
memes = [
    {"image": "https://i.imgur.com/OuKDd6T.jpeg", "caption": "Когда ОЛЕГ шутит 😹"},
    {"image": "https://i.imgur.com/Zb1rkuF.jpeg", "caption": "Когда угадал число с 1 раза 🎯"},
    {"image": "https://i.imgur.com/YlHbNZx.jpeg", "caption": "Ответ на 'как дела' 🤠"},
    {"image": "https://i.imgur.com/u7nGlNd.jpeg", "caption": "Типичный пользователь бота ОЛЕГ 🤖"},
    {"image": "https://i.imgur.com/R6KdZ1p.jpeg", "caption": "Когда бот в отпуске 🏖️"}
]

# 🎬 Рекомендованные фильмы — по жанрам: список фильмов
movies = {
    "боевик": [  # жанр "боевик"
        {"title": "Терминатор 2", "desc": "Классика жанра 💥", "img": "https://i.imgur.com/2D2fO8U.jpeg"},
        {"title": "Джон Уик", "desc": "Месть, стиль и собака 🐕", "img": "https://i.imgur.com/mjHoUBo.jpeg"}
    ],
    "комедия": [  # жанр "комедия"
        {"title": "Один дома", "desc": "Кевин опять забыл родителей 😂", "img": "https://i.imgur.com/Xcc0GIM.jpeg"},
        {"title": "Маска", "desc": "Смех, зелёное лицо и Джим Керри 🟢", "img": "https://i.imgur.com/y10iBGP.jpeg"}
    ],
    "ужасы": [  # жанр "ужасы"
        {"title": "Пила", "desc": "Игра на выживание 🪚", "img": "https://i.imgur.com/0u3pHzC.jpeg"},
        {"title": "Астрал", "desc": "Когда дом не просто скрипит 👻", "img": "https://i.imgur.com/j5Ub6Pq.jpeg"}
    ]
}

# ❓ Вопросы для викторины: текст вопроса, варианты ответов и правильный ответ
quiz = [
    {"question": "Сколько будет 3 + 5?", "options": ["6", "8", "10"], "correct": "8"},
    {"question": "Какой язык у бота ОЛЕГ?", "options": ["C++", "Python", "HTML"], "correct": "Python"},
    {"question": "Кто главный герой фильма 'Матрица'?", "options": ["Нео", "Морфеус", "Тринити"], "correct": "Нео"}
]

# 💬 Ответы на фразы пользователя. Используются случайные варианты для разнообразия
responses = {
    "привет": ["Здарова! 😎", "Привет-привет! 👋", "Хэй, как жизнь? 🧢"],
    "как дела": ["Как огурец! 🥒", "Всё пучком 🌈", "Нормально, а у тебя?"],
    "что делаешь": ["Да ниче, байты гоняю 📡", "Сижу в чатах как обычно 🤖", "Работаю ботом 24/7 😅"]
}

# ⌨️ Главное меню — кнопки для быстрого доступа к функциям
main_menu = ReplyKeyboardMarkup([
    [KeyboardButton("👋 Привет"), KeyboardButton("😂 Шутка")],
    [KeyboardButton("🎬 Фильм"), KeyboardButton("🎮 Игра")],
    [KeyboardButton("📊 Викторина"), KeyboardButton("📷 Мем")],
    [KeyboardButton("🤔 Как дела?"), KeyboardButton("🙋 Что делаешь?")],
    [KeyboardButton("👋 Пока")]
], resize_keyboard=True)

# 👋 Обработчик команды /start — запускается при первом запуске бота пользователем
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Если счётчик побед ещё не создан — создаём его
    context.user_data.setdefault("wins", 0)
    # Отправляем приветственное сообщение и показываем главное меню
    await update.message.reply_text("Привет, я ОЛЕГ 🤖 Жми кнопки, веселись!", reply_markup=main_menu)

# 🧠 Отправляем пользователю случайный вопрос викторины с вариантами кнопок-ответов
async def send_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = choice(quiz)  # случайный вопрос из списка
    # создаём кнопки — каждая содержит callback_data с правильным и выбранным ответом
    buttons = [InlineKeyboardButton(opt, callback_data=f"answer|{q['correct']}|{opt}") for opt in q["options"]]
    # отправляем вопрос с кнопками пользователю
    await update.message.reply_text(q["question"], reply_markup=InlineKeyboardMarkup.from_column(buttons))

# ✅ Обработка нажатия на кнопку в викторине — сравниваем ответы
async def check_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query  # объект нажатия
    await query.answer()  # подтверждаем получение
    _, correct, selected = query.data.split("|")  # разбираем данные
    if selected == correct:
        await query.edit_message_text("✅ Верно! Молодец!")
    else:
        await query.edit_message_text(f"❌ Нет, правильный ответ: {correct}")

# 📩 Обрабатываем любое сообщение от пользователя
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()  # переводим сообщение в нижний регистр

    # Проверка на ключевые слова в сообщении — выбираем соответствующую реакцию
    if "привет" in text:
        await update.message.reply_text(choice(responses["привет"]))
    elif "как дела" in text:
        await update.message.reply_text(choice(responses["как дела"]))
    elif "что делаешь" in text:
        await update.message.reply_text(choice(responses["что делаешь"]))
    elif "шутка" in text:
        await update.message.reply_text(choice(jokes))
    elif "мем" in text:
        meme = choice(memes)
        await update.message.reply_photo(photo=meme["image"], caption=meme["caption"])
    elif "фильм" in text:
        genre = choice(list(movies.keys()))  # выбираем случайный жанр
        movie = choice(movies[genre])  # фильм из этого жанра
        msg = f"🎬 <b>{movie['title']}</b>\n{movie['desc']}"
        await update.message.reply_photo(photo=movie["img"], caption=msg, parse_mode="HTML")
    elif "викторина" in text:
        await send_quiz(update, context)
    elif "игра" in text:
        # Запуск мини-игры "Угадай число"
        context.user_data["guess"] = randint(1, 100)  # сохраняем загаданное число
        context.user_data["tries"] = 5  # даём 5 попыток
        await update.message.reply_text("Угадай число от 1 до 100 🎯 (у тебя 5 попыток)")
    elif "guess" in context.user_data:
        # Если уже идёт игра — обрабатываем число
        try:
            num = int(text)
        except:
            await update.message.reply_text("Напиши число 🧮")
            return

        context.user_data["tries"] -= 1  # уменьшаем попытки
        answer = context.user_data["guess"]

        if num == answer:
            context.user_data["wins"] += 1
            await update.message.reply_text(f"✅ Угадал! Побед: {context.user_data['wins']}")
            context.user_data.pop("guess")
        elif context.user_data["tries"] == 0:
            await update.message.reply_text(f"❌ Не угадал. Было число: {answer}")
            context.user_data.pop("guess")
        else:
            hint = "меньше" if num > answer else "больше"
            await update.message.reply_text(f"Число {hint}. Осталось попыток: {context.user_data['tries']}")
    elif "пока" in text:
        await update.message.reply_text("Пока! 👋", reply_markup=main_menu)
    else:
        await update.message.reply_text("Не понял тебя 🧐 Нажми кнопку ⬇️")

# ▶️ Функция для запуска Telegram-бота
def run_bot():
    app = Application.builder().token("ВСТАВЬ СЮДА СВОЙ ТОКЕН").build()  # создаём приложение с токеном

    # Регистрируем обработчики команд и сообщений
    app.add_handler(CommandHandler("start", start))  # /start
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  # обычные тексты
    app.add_handler(CallbackQueryHandler(check_quiz))  # нажатия по кнопкам викторины

    print("Бот запущен ✅")
    app.run_polling()  # запускаем бота (режим ожидания новых сообщений)

# ⬇️ Старт бота
run_bot()
