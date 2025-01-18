#pip install kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

def wrong():
    print('Сам ты белый')

def correct():
    print('Теперь ты негр')


class MyApp(App):
    def build(self):
        
        label = Label(text='Какого цвета чернокожий?', font_size='60px')
        button = Button(text='Белый', size_hint=(0.8, 0.4), color=(1,1,1,1))
        button2 = Button(text='Черный', size_hint=(0.8, 0.4), color=(0,0,0,1))

        button.on_press = wrong
        button2.on_press = correct

        layout = BoxLayout(orientation='vertical')
        button_layout = BoxLayout()

        layout.add_widget(label)
        button_layout.add_widget(button)
        button_layout.add_widget(button2)
        layout.add_widget(button_layout)

        return layout

app = MyApp()
app.run()
