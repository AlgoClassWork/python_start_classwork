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
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 60
        self.padding = [10, 10, 10, 10]
        self.spacing = 10

        checkbox = CheckBox(active=self.task['completed'], color=get_color_from_hex('#FFFFFF'))
        checkbox.bind(active=self.on_checkbox_active)

        self.label = Label(text=self.task['description'], markup=True, font_size=18, color=get_color_from_hex('#FFFFFF'))

class TodoApp(App):
    def build(self):
        self.tasks = []  

        root = FloatLayout()

        input_layout = BoxLayout(orientation='horizontal', size_hint=(0.9, None), height=50, pos_hint={'center_x': 0.5, 'top': 0.95})
        self.text_input = TextInput(multiline=False, background_color=get_color_from_hex('#333333'), foreground_color=get_color_from_hex('#FFFFFF'), font_size=18)
        add_button = Button(text='Add', size_hint=(None, None), size=(100, 50), background_color=get_color_from_hex('#4CAF50'), color=get_color_from_hex('#FFFFFF'))
        add_button.bind(on_press=self.add_task)
        input_layout.add_widget(self.text_input)
        input_layout.add_widget(add_button)

    def add_task(self, instance):
        task_text = self.text_input.text.strip()
        if task_text:
            task = {'description': task_text, 'completed': False}
            self.tasks.append(task)
            task_widget = TaskWidget(task=task, tasks_list=self.tasks)
            

app = ToDoApp()
app.run()
