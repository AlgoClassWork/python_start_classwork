from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

from kivy.properties import ObjectProperty
from kivy.core.window import Window

Window.clearcolor = (0.3, 0.3, 0.9, 1)

class ImageButton(ButtonBehavior, Image):
    pass

class TaskWidget(BoxLayout):
    task = ObjectProperty(None)
    tasks_list = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.height = 60

        checkbox = CheckBox(active=self.task['completed'])
        self.label = Label(text=self.task['description'], markup=True, font_size=18)
        delete_button = ImageButton(source='delete_icon.png', size_hint=(None, None), size=(30, 30))

        self.add_widget(checkbox)
        self.add_widget(self.label)
        self.add_widget(delete_button)

        checkbox.bind(active=self.checkbox_activate)

    def checkbox_activate(self, instance, value):
        self.task['completed'] = value
        self.update_label()

    def update_label(self):
        if self.task['completed']:
            self.label.text = f'[s] {self.task['description']} [/s]'
        else:
            self.label.text = f' {self.task['description']} '


class TodoApp(App):
    def build(self):
        self.tasks = []  

        root = FloatLayout()

        self.input_layout = BoxLayout(orientation='horizontal', size_hint=(0.9, None), height=50, pos_hint={'center_x': 0.5, 'top': 0.95})
        self.text_input = TextInput(multiline=False, font_size=18)
        add_button = Button(text='Add', size_hint=(None, None), size=(100, 50))
        add_button.bind(on_press=self.add_task)
        self.input_layout.add_widget(self.text_input)
        self.input_layout.add_widget(add_button)

        self.tasks_layout = GridLayout(cols=1, spacing=10, size_hint_y = None)
        self.tasks_layout.bind(minimum_height=self.tasks_layout.setter('height'))
        scroll_view = ScrollView(size_hint=(1, 1), pos_hint={'center_x':0.4, 'center_y':0.4})
        scroll_view.add_widget(self.tasks_layout)

        root.add_widget(self.input_layout)
        root.add_widget(scroll_view)

        return root

    def add_task(self, instance):
        task_text = self.text_input.text.strip()
        if task_text:
            task = {'description': task_text, 'completed': False}
            self.tasks.append(task)
            task_widget = TaskWidget(task=task, tasks_list=self.tasks)
            self.tasks_layout.add_widget(task_widget)
 
app = TodoApp()
app.run()
