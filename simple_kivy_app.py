from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.widget import Widget

# Установка фонового цвета окна
Window.clearcolor = (0.95, 0.95, 1, 1)  # Светло-голубой фон

# Кастомные стили
BUTTON_STYLE = {
    'font_size': '24sp',
    'background_normal': '',
    'background_color': (0.2, 0.6, 1, 1),  # Насыщенно-синий
    'color': (1, 1, 1, 1),  # Белый текст
    'size_hint': (0.6, 0.2),
    'pos_hint': {'center_x': 0.5}
}

LABEL_STYLE = {
    'font_size': '32sp',
    'color': (0.1, 0.1, 0.4, 1)  # Тёмно-синий
}

PADDING = 50
SPACING = 30

class FirstScreen(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)
        layout = BoxLayout(orientation='vertical', padding=PADDING, spacing=SPACING)

        label = Label(text='Первый экран', **LABEL_STYLE)
        button = Button(text='Перейти', **BUTTON_STYLE)
        button.on_press = self.next

        layout.add_widget(Widget(size_hint_y=0.3))  # отступ сверху
        layout.add_widget(label)
        layout.add_widget(button)
        layout.add_widget(Widget(size_hint_y=0.3))  # отступ снизу

        self.add_widget(layout)

    def next(self):
        self.manager.current = 'second'
        self.manager.transition.direction = 'left'
        
class SecondScreen(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        layout = BoxLayout(orientation='vertical', padding=PADDING, spacing=SPACING)

        label = Label(text='Второй экран', **LABEL_STYLE)
        button = Button(text='Перейти', **BUTTON_STYLE)
        button.on_press = self.next

        layout.add_widget(Widget(size_hint_y=0.3))
        layout.add_widget(label)
        layout.add_widget(button)
        layout.add_widget(Widget(size_hint_y=0.3))

        self.add_widget(layout)

    def next(self):
        self.manager.current = 'first'
        self.manager.transition.direction = 'right'

class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(FirstScreen())
        screen_manager.add_widget(SecondScreen())
        return screen_manager

app = MyApp()
app.run()
