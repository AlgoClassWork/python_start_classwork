from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window


# Задаем главный цвет нашего приложения
Window.clearcolor = (0.95,0.95,1,1)


class StartScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical',padding=20, spacing=20)
        title_label = Label(text='Тест на слабоумие',font_size='60px', color=(0,0,0,1))
        description_label = Label(text= 'Это шуточный тест.\n'
                                        'Он не претендует на медецинскую точность\n'
                                        'Пройдите его, чтобы узнать свой результат!',
        font_size='30px', color=(0,0,0,1), halign = 'center')
        start_button = Button(text='Начать тест',
                              size_hint=(0.5,0.2),
                              pos_hint={'center_x': 0.5},
                              background_color = (0,0,0,1))
        layout.add_widget(title_label)
        layout.add_widget(description_label)
        layout.add_widget(start_button)
        self.add_widget(layout)


class TestApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(StartScreen(name='start_screen'))
        return screen_manager

app = TestApp()
app.run()
