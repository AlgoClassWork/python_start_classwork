from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class ToDoApp(App):
    def build(self):
        input_layout = BoxLayout()
        self.text_input = TextInput(font_size=30)
        add_button = Button(text='Добавить')
        input_layout.add_widget(self.text_input)
        input_layout.add_widget(add_button)
        return input_layout

app = ToDoApp()
app.run()
