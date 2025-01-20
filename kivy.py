from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class TestApp(App):
    def build(self):
        label = Label(text='Какого цвета чернокожие?', font_size='50px')
        button = Button(text='Белый', size_hint=(1,0.5))
        button2 = Button(text='Черный', size_hint=(1,0.5))
        layout = BoxLayout(orientation='vertical')
        layout_button = BoxLayout()
        layout_button.add_widget(button)
        layout_button.add_widget(button2)
        layout.add_widget(label)
        layout.add_widget(layout_button)
        return layout

app = TestApp()
app.run()
