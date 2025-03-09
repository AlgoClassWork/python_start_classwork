from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.properties import ObjectProperty

class Task(BoxLayout):
    task = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        checkbox = CheckBox()
        self.label = Label(text=self.task['описание'])
        self.add_widget(checkbox)
        self.add_widget(self.label)

class ToDoApp(App):
    def build(self):
        self.input_layout = BoxLayout(size_hint=(0.95, 0.1), pos_hint={'center_x': 0.5, 'top': 0.95 })
        self.text_input = TextInput(font_size=30)
        add_button = Button(text='Добавить', size_hint=(0.15, 0.95), background_color=(0.3,1,0.3,1))
        add_button.on_press = self.add_task
        self.input_layout.add_widget(self.text_input)
        self.input_layout.add_widget(add_button)
        return self.input_layout
    
    def add_task(self):
        task_text = self.text_input.text.strip()
        if task_text:
            task = {'описание': task_text, 'статус': False}
            task_widgget = Task(task=task)
            self.input_layout.add_widget(task_widgget)
            

app = ToDoApp()
app.run()
