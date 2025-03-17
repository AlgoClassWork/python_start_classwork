from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)

class ToDoApp(App):
    def build(self):
        self.text_input = TextInput(font_size=30)
        add_button = Button(text='Добавить', size_hint=(0.3, 1),
        font_size=30, background_color=(0.7, 1, 0.7, 1) )

        self.input_layout = BoxLayout(size_hint=(1, 0.1),
        pos_hint={'center_y':0.95}, spacing='10px')
        
        self.input_layout.add_widget(self.text_input)
        self.input_layout.add_widget(add_button)
        return self.input_layout
    
app = ToDoApp()
app.run()
