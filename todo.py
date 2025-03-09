from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class ToDoApp(App):
    def build(self):
        text = TextInput(font_size=30)
        button = Button(text='Добавить',  size_hint=(None, None), size=(100,50), background_color=(0.5,1,0.5,1))
        layout = BoxLayout(size_hint=(0.9, None),  height=50, pos_hint={'center_x':0.5, 'top': 0.95},)
        layout.add_widget(text)
        layout.add_widget(button)

        return layout

app = ToDoApp()
app.run()
