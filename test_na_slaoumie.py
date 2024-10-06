import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.clearcolor = (0.95, 0.95, 1, 1)  # Светло-голубой фон

# Стартовый экран с приветствием и кнопкой начала теста
class StartScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Заголовок приложения
        title_label = Label(text="Тест на слабоумие", font_size='32sp', color=(0, 0, 0, 1))
        layout.add_widget(title_label)
        
        # Описание/инструкция
        description_label = Label(
            text="Это шуточный тест. Он не претендует на медицинскую точность!\n"
                 "Пройдите тест, чтобы узнать свой \"результат\"!",
            font_size='18sp',
            color=(0, 0, 0, 1),
            halign="center"
        )
        layout.add_widget(description_label)

        # Кнопка для начала теста
        start_button = Button(
            text="Начать тест",
            size_hint=(0.5, 0.2),
            pos_hint={'center_x': 0.5},
            background_color=(0.3, 0.7, 1, 1),
            color=(1, 1, 1, 1)
        )
        start_button.bind(on_press=self.start_test)  # Связываем кнопку с функцией начала теста
        layout.add_widget(start_button)

        self.add_widget(layout)

    # Функция для начала теста (переход к первому вопросу)
    def start_test(self, instance):
        app = App.get_running_app()
        app.sm.current = 'question_0'  # Переход к первому вопросу


# Экран для отображения вопросов
class QuestionScreen(Screen):
    def __init__(self, question_data, question_index, **kwargs):
        super().__init__(**kwargs)
        self.name = f'question_{question_index}'  # Уникальное имя для каждого экрана
        self.question_data = question_data
        self.question_index = question_index

        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Текст вопроса
        question_label = Label(text=question_data["question"], font_size='24sp', color=(0, 0, 0, 1))
        layout.add_widget(question_label)

        # Кнопки с вариантами ответов
        for option in question_data["options"]:
            answer_button = Button(
                text=option["text"],
                size_hint=(0.8, 0.2),
                pos_hint={'center_x': 0.5},
                background_color=(0.3, 0.7, 1, 1),
                color=(1, 1, 1, 1)
            )
            answer_button.bind(on_press=lambda instance, option=option: self.check_answer(option))
            layout.add_widget(answer_button)

        self.add_widget(layout)

    # Обрабатываем выбранный ответ
    def check_answer(self, option):
        app = App.get_running_app()
        app.user_answers.append(option["correct"])  # Сохраняем результат ответа

        if self.question_index < len(app.questions) - 1:
            # Переходим к следующему вопросу
            next_screen_name = f'question_{self.question_index + 1}'
            app.sm.current = next_screen_name
        else:
            # Если это был последний вопрос, показываем результат
            app.sm.current = 'result_screen'


# Экран с результатом теста
class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'result_screen'
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Метка для текста результата
        self.result_label = Label(text="", font_size='24sp', color=(0, 0, 0, 1))
        self.layout.add_widget(self.result_label)

        # Кнопка для повторного прохождения теста
        retry_button = Button(
            text="Попробовать снова",
            size_hint=(0.8, 0.2),
            pos_hint={'center_x': 0.5},
            background_color=(0.3, 0.7, 1, 1),
            color=(1, 1, 1, 1)
        )
        retry_button.bind(on_press=self.retry_test)  # Связываем кнопку с перезапуском теста
        self.layout.add_widget(retry_button)

        self.add_widget(self.layout)

    def on_enter(self):
        # Вычисляем результат на основе ответов пользователя
        app = App.get_running_app()
        correct_answers = sum(app.user_answers)
        total_questions = len(app.questions)

        if correct_answers == total_questions:
            result_text = "Вы гений! Наверное..."
        elif correct_answers > total_questions // 2:
            result_text = "Не беспокойтесь, всё в пределах нормы."
        else:
            result_text = "Что ж, возможно, стоит задуматься!"

        self.result_label.text = f"Ваш результат: {result_text}"

    def retry_test(self, instance):
        # Перезапускаем тест
        app = App.get_running_app()
        app.user_answers = []  # Сбрасываем ответы
        app.sm.current = 'start_screen'  # Возвращаемся на стартовый экран


# Основное приложение
class TestApp(App):
    def build(self):
        with open('questions.json', 'r', encoding='utf-8') as f:
            self.questions = json.load(f)
        
        self.user_answers = []  # Список для хранения ответов
        self.sm = ScreenManager()

        # Добавляем стартовый экран
        self.sm.add_widget(StartScreen(name='start_screen'))

        # Добавляем экраны для всех вопросов
        for index, question in enumerate(self.questions):
            screen = QuestionScreen(question_data=question, question_index=index)
            self.sm.add_widget(screen)

        # Добавляем экран результатов
        self.sm.add_widget(ResultScreen())

        # Устанавливаем начальный экран
        self.sm.current = 'start_screen'

        return self.sm



if __name__ == '__main__':
    TestApp().run()
