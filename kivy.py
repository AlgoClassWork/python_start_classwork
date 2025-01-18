#pip install kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        
        label = Label(text='Какого цвета чернокожий?', font_size='60px')
        button = Button(text='Белый')
        button2 = Button(text='Розовый')

        layout = BoxLayout(orientation='vertical')
        button_layout = BoxLayout()

        layout.add_widget(label)
        button_layout.add_widget(button)
        button_layout.add_widget(button2)
        layout.add_widget(button_layout)

        return layout

app = MyApp()
app.run()
