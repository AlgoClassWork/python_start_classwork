from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image 

from kivy.animation import Animation
from kivy.properties import ObjectProperty
from kivy.utils import get_color_from_hex
from kivy.core.window import Window

Window.clearcolor = (0.5,0.5,1,1)

class ImageButton(ButtonBehavior, Image):
    pass

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
        delete_button = ImageButton(source='delete_icon.png', size_hint=(None, None), size=(30,30))
        delete_button.bind(on_press=self.delete_task)

        self.add_widget(checkbox)
        self.add_widget(self.label)
        self.add_widget(delete_button)

    def on_checkbox_active(self, instance, value):
        self.task['completed'] = value
        self.update_label()

    def update_label(self):
        if self.task['completed']:
            self.label.text = f"[s]{self.task['description']}[/s]"
        else:
            self.label.text = f"{self.task['description']}"

    def delete_task(self, instance):
        if self.task in self.tasks_list:
            self.tasks_list.remove(self.task)

        instance.disabled = True
        anim = Animation(opacity=0, duration=0.3)
        anim.bind(on_complete=lambda *args: self.parent.remove_widget(self))
        anim.start(self)

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

        self.tasks_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.tasks_layout.bind(minimum_height=self.tasks_layout.setter('height'))
        scroll_view = ScrollView(size_hint=(0.9, 0.8), pos_hint={'center_x':0.5, 'center_y':0.5})
        scroll_view.add_widget(self.tasks_layout)

        root.add_widget(input_layout)
        root.add_widget(scroll_view)

        return root

    def add_task(self, instance):
        task_text = self.text_input.text.strip()
        if task_text:
            task = {'description': task_text, 'completed': False}
            self.tasks.append(task)
            task_widget = TaskWidget(task=task, tasks_list=self.tasks)
            self.tasks_layout.add_widget(task_widget)
            self.text_input.text = ''
            task_widget.opacity = 0
            Animation(opacity=1, duration=0.3).start(task_widget)
            
app = TodoApp()
app.run()
