from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

def test():
    print('Событие!')

class MyApp(App):
    def build(self):
        txt = Label(text='Это надпись')
        btn = Button(text='Это кнопка')
        btn.on_press = test 
        layout = BoxLayout()
        layout.add_widget(txt)
        layout.add_widget(btn)
        return layout

MyApp().run()
