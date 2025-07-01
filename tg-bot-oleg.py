from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
from random import choice, shuffle, randint

# 📌 Это список случайных шуток, которые бот может отправлять при соответствующем запросе
шутки = [
    "Колобок повесился 😂", "Русалка села на шпагат 🧜‍♀️", "Рыба утонула 🐟",
    "Грабитель вернул кошелёк, когда узнал баланс 💸", "Слон сел на Wi-Fi 🐘📶",
    "Программист пошёл на свидание — сделал rollback 🫣", "В носках дырки от пользователей 😅",
    "Когда упал интернет — я снова увидел свою семью 👨‍👩‍👧‍👦", "Я не ленивая, я в энергосберегающем режиме 🔋",
    "Почему кофе не отвечает? Потому что он молчит... ☕😶"
]

# 📌 Список мемов — каждый мем содержит ссылку на картинку и текст для подписи
мемы = [
    {"url": "https://i.imgur.com/OuKDd6T.jpeg", "текст": "Когда ОЛЕГ шутит 😹"},
    {"url": "https://i.imgur.com/Zb1rkuF.jpeg", "текст": "Когда угадал число с 1 раза 🎯"},
    {"url": "https://i.imgur.com/YlHbNZx.jpeg", "текст": "Ответ на 'как дела' 🤠"},
    {"url": "https://i.imgur.com/u7nGlNd.jpeg", "текст": "Типичный пользователь бота ОЛЕГ 🤖"},
    {"url": "https://i.imgur.com/R6KdZ1p.jpeg", "текст": "Когда бот в отпуске 🏖️"}
]

# 📌 Рекомендованные фильмы по жанрам. Каждый фильм содержит название, описание и ссылку на постер
фильмы = {
    "боевик": [
        {"название": "Терминатор 2", "описание": "Классика жанра 💥", "картинка": "https://i.imgur.com/2D2fO8U.jpeg"},
        {"название": "Джон Уик", "описание": "Месть, стиль и собака 🐕", "картинка": "https://i.imgur.com/mjHoUBo.jpeg"}
    ],
    "комедия": [
        {"название": "Один дома", "описание": "Кевин опять забыл родителей 😂", "картинка": "https://i.imgur.com/Xcc0GIM.jpeg"},
        {"название": "Маска", "описание": "Смех, зелёное лицо и Джим Керри 🟢", "картинка": "https://i.imgur.com/y10iBGP.jpeg"}
    ],
    "ужасы": [
        {"название": "Пила", "описание": "Игра на выживание 🪚", "картинка": "https://i.imgur.com/0u3pHzC.jpeg"},
        {"название": "Астрал", "описание": "Когда дом не просто скрипит 👻", "картинка": "https://i.imgur.com/j5Ub6Pq.jpeg"}
    ]
}

# 📌 Вопросы для викторины. Каждый вопрос содержит список вариантов и правильный ответ
вопросы_викторины = [
    {"вопрос": "Сколько будет 3 + 5?", "ответы": ["6", "8", "10"], "правильный": "8"},
    {"вопрос": "Какой язык у бота ОЛЕГ?", "ответы": ["C++", "Python", "HTML"], "правильный": "Python"},
    {"вопрос": "Кто главный герой фильма 'Матрица'?", "ответы": ["Нео", "Морфеус", "Тринити"], "правильный": "Нео"}
]

# 📌 Вариативные ответы для приветствий и вопросов — для разнообразия фраз
варианты_ответа = {
    "привет": ["Здарова! 😎", "Привет-привет! 👋", "Хэй, как жизнь? 🧢"],
    "как дела": ["Как огурец! 🥒", "Всё пучком 🌈", "Нормально, а у тебя?"],
    "что делаешь": ["Да ниче, байты гоняю 📡", "Сижу в чатах как обычно 🤖", "Работаю ботом 24/7 😅"]
}

# 📌 Главное меню с кнопками. Кнопки отображаются пользователю для быстрого выбора
меню = ReplyKeyboardMarkup([
    [KeyboardButton("👋 Привет"), KeyboardButton("😂 Шутка")],
    [KeyboardButton("🎬 Фильм"), KeyboardButton("🎮 Игра")],
    [KeyboardButton("📊 Викторина"), KeyboardButton("📷 Мем")],
    [KeyboardButton("🤔 Как дела?"), KeyboardButton("🙋 Что делаешь?")],
    [KeyboardButton("👋 Пока")]
], resize_keyboard=True)

# 📌 Функция, которая запускается при команде /start — показывает приветствие и кнопки
async def начать(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.setdefault("победы", 0)  # создаёт счётчик побед, если его ещё нет
    await update.message.reply_text("Привет, я ОЛЕГ 🤖 Жми кнопки, веселись!", reply_markup=меню)

# 📌 Отправка пользователю случайного вопроса из викторины с кнопками-ответами
async def отправить_викторину(update: Update, context: ContextTypes.DEFAULT_TYPE):
    вопрос = choice(вопросы_викторины)
    кнопки = [InlineKeyboardButton(ответ, callback_data=f"ответ|{вопрос['правильный']}|{ответ}") for ответ in вопрос["ответы"]]
    await update.message.reply_text(вопрос["вопрос"], reply_markup=InlineKeyboardMarkup.from_column(кнопки))

# 📌 Обработка нажатия на кнопку ответа в викторине — проверяем правильность
async def проверка_викторины(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    _, правильный, выбранный = query.data.split("|")
    if правильный == выбранный:
        await query.edit_message_text("✅ Верно! Молодец!")
    else:
        await query.edit_message_text(f"❌ Нет, правильный ответ: {правильный}")

# 📌 Основная функция обработки всех входящих текстов от пользователя
async def обработать_сообщение(update: Update, context: ContextTypes.DEFAULT_TYPE):
    текст = update.message.text.lower()  # Переводим в нижний регистр для простоты сравнения

    # обрабатываем разные команды пользователя
    if "привет" in текст:
        await update.message.reply_text(choice(варианты_ответа["привет"]))
    elif "как дела" in текст:
        await update.message.reply_text(choice(варианты_ответа["как дела"]))
    elif "что делаешь" in текст:
        await update.message.reply_text(choice(варианты_ответа["что делаешь"]))
    elif "шутка" in текст:
        await update.message.reply_text(choice(шутки))
    elif "мем" in текст:
        мем = choice(мемы)
        await update.message.reply_photo(photo=мем["url"], caption=мем["текст"])
    elif "фильм" in текст:
        жанры = list(фильмы.keys())
        выбранный_жанр = choice(жанры)
        фильм = choice(фильмы[выбранный_жанр])
        текст_фильма = f"🎬 <b>{фильм['название']}</b>\n{фильм['описание']}"
        await update.message.reply_photo(photo=фильм["картинка"], caption=текст_фильма, parse_mode="HTML")
    elif "викторина" in текст:
        await отправить_викторину(update, context)
    elif "игра" in текст:
        число = randint(1, 100)
        context.user_data["число"] = число  # сохраняем загаданное число
        context.user_data["попытки"] = 5     # и количество попыток
        await update.message.reply_text("Угадай число от 1 до 100 🎯 (у тебя 5 попыток)")
    elif "число" in context.user_data:
        try:
            введено = int(текст)
        except:
            await update.message.reply_text("Напиши число 🧮")
            return
        context.user_data["попытки"] -= 1
        число = context.user_data["число"]
        if введено == число:
            context.user_data["победы"] += 1
            await update.message.reply_text(f"✅ Угадал! Побед: {context.user_data['победы']}")
            context.user_data.pop("число")
        elif context.user_data["попытки"] == 0:
            await update.message.reply_text(f"❌ Не угадал. Было число: {число}")
            context.user_data.pop("число")
        else:
            подсказка = "меньше" if введено > число else "больше"
            await update.message.reply_text(f"Число {подсказка}. Осталось попыток: {context.user_data['попытки']}")
    elif "пока" in текст:
        await update.message.reply_text("Пока! 👋", reply_markup=меню)
    else:
        await update.message.reply_text("Не понял тебя 🧐 Нажми кнопку ⬇️")

# 📌 Функция запуска бота — настраивает токен и подключает обработчики

бот = Application.builder().token("ТОКЕН").build()  # ⛔ Заменить на реальный токен из @BotFather
бот.add_handler(CommandHandler("start", начать))  # обработчик команды /start
бот.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, обработать_сообщение))  # текстовые сообщения
бот.add_handler(CallbackQueryHandler(проверка_викторины))  # кнопки викторины
print("Бот запущен ✅")
бот.run_polling()  # запуск бота — он ждёт входящих сообщений
