from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label

from kivy.properties import ObjectProperty

class TaskWidget(BoxLayout):
    task = ObjectProperty(None)
    tasks_list = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        checkbox = CheckBox(active=self.task['completed'])
        self.label = Label(text=self.task['description'], markup=True, font_size=18)

        self.add_widget(checkbox)
        self.add_widget(self.label)


class TodoApp(App):
    def build(self):
        self.tasks = []  

        root = BoxLayout()

        self.input_layout = BoxLayout(orientation='horizontal', size_hint=(0.9, None), height=50, pos_hint={'center_x': 0.5, 'top': 0.95})
        self.text_input = TextInput(multiline=False, font_size=18)
        add_button = Button(text='Add', size_hint=(None, None), size=(100, 50))
        add_button.bind(on_press=self.add_task)
        self.input_layout.add_widget(self.text_input)
        self.input_layout.add_widget(add_button)

        root.add_widget(self.input_layout)

        return root

    def add_task(self, instance):
        task_text = self.text_input.text.strip()
        if task_text:
            task = {'description': task_text, 'completed': False}
            self.tasks.append(task)
            task_widget = TaskWidget(task=task, tasks_list=self.tasks)
            self.input_layout.add_widget(task_widget)

            
app = TodoApp()
app.run()
