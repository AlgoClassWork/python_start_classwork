from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class TestApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')
        title_label = Label(text='Тест на слабоумие')
        description_label = Label(text='Тест не претендует на медецинскую точность')
        start_button = Button(text='Начать тест')
        layout.add_widget(title_label)
        layout.add_widget(description_label)
        layout.add_widget(start_button)
        return layout

app = TestApp()
app.run()
