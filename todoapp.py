from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label

class Task(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        checkbox = CheckBox(activate=False)
        self.label = Label(text=self.task['описание'])
        self.add_widget(checkbox)
        self.add_widget(self.label)

class ToDoApp(App):
    def build(self):
        input_layout = BoxLayout(size_hint=(0.95, 0.1), pos_hint={'center_x': 0.5, 'top': 0.95 })
        self.text_input = TextInput(font_size=30)
        add_button = Button(text='Добавить', size_hint=(0.15, 0.95), background_color=(0.3,1,0.3,1))
        add_button.on_press = self.add_task
        input_layout.add_widget(self.text_input)
        input_layout.add_widget(add_button)
        return input_layout
    
    def add_task(self):
        task_text = self.text_input.text.strip()
        if task_text:
            task = {'описание': task_text, 'статус': False}
            #task_widgget = TaskWidget(task)

app = ToDoApp()
app.run()
