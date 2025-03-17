from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label

from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)

class TaskWidget(BoxLayout):
    def __init__(self, **data):
        super().__init__()
        checkbox = CheckBox()
        self.label = Label(text='здесь будет ваша задача')
        delete_button = Button(text='удалить')

        self.add_widget(checkbox)
        self.add_widget(self.label)
        self.add_widget(delete_button)

class ToDoApp(App):
    def build(self):
        self.text_input = TextInput(font_size=30)
        add_button = Button(text='Добавить', size_hint=(0.3, 1),
        font_size=30, background_color=(0.7, 1, 0.7, 1) )
        add_button.on_press = self.add_task
        self.input_layout = BoxLayout(size_hint=(1, 0.1),
        pos_hint={'center_y':0.95}, spacing='10px')
        
        self.input_layout.add_widget(self.text_input)
        self.input_layout.add_widget(add_button)
        return self.input_layout
    
    def add_task(self):
        task_text = self.text_input.text.strip()
        if task_text:
            task_widget = TaskWidget()
            self.input_layout.add_widget(task_widget)
    
app = ToDoApp()
app.run()
