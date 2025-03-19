from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from kivy.core.window import Window
from kivy.animation import Animation
from kivy.properties import ObjectProperty

Window.clearcolor = (1,1,1,1)

class TaskWidget(BoxLayout):
    task = ObjectProperty(None)
    tasks = ObjectProperty(None)

    def __init__(self, **data):
        super().__init__(**data)
        self.size_hint_y = None
        self.height = 50

        checkbox = CheckBox(size_hint=(0.1, 1))
        self.label = Label(text=self.task['описание'], color=(0,0,0,1), font_size=30)
        delete_button = Button(text='Удалить', size_hint=(0.33, 1),
        background_color=(1, 0.5, 0.5, 1), font_size=30)

        self.add_widget(checkbox)
        self.add_widget(self.label)
        self.add_widget(delete_button)

        checkbox.bind(active=self.checkbox_activate)
        delete_button.bind(on_press=self.delete_task)

    def delete_task(self, instance):
        if self.task in self.tasks:
            self.tasks.remove(self.task)

        instance.disabled = True
        animation = Animation(opacity=0, duration=1)
        animation.bind(on_complete=lambda *data: self.parent.remove_widget(self))
        animation.start(self)

    def checkbox_activate(self, instance, value):
        self.task['статус'] = value
        self.update_label()

    def update_label(self):
        if self.task['статус']:
            self.label.text = f'Выполнено: {self.task['описание']} '
        else:
            self.label.text = f' {self.task['описание']} '


class ToDoApp(App):
    def build(self):
        self.tasks = []

        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.text_input = TextInput(font_size=30)
        add_button = Button(text='Добавить', size_hint=(0.3, 1),
        font_size=30, background_color=(0.7, 1, 0.7, 1) )
        add_button.on_press = self.add_task
        self.input_layout = BoxLayout(size_hint=(1, 0.1),
        pos_hint={'center_y':0.95}, spacing='10px')

        self.tasks_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        self.tasks_layout.bind(minimum_height=self.tasks_layout.setter('height'))
        scroll_view = ScrollView(pos_hint={'center_y':0.4})
        scroll_view.add_widget(self.tasks_layout)
        
        self.input_layout.add_widget(self.text_input)
        self.input_layout.add_widget(add_button)

        main_layout.add_widget(self.input_layout)
        main_layout.add_widget(scroll_view)

        return main_layout
    
    def add_task(self):
        task_text = self.text_input.text.strip()
        if task_text:
            task = {'описание': task_text, 'статус': False}
            self.tasks.append(task)
            task_widget = TaskWidget(task = task, tasks = self.tasks)
            self.tasks_layout.add_widget(task_widget)
            self.text_input.text = ''
            task_widget.opacity = 0
            Animation(opacity=1, duration=1).start(task_widget)
    
app = ToDoApp()
app.run()

