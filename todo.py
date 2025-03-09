from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.properties import ObjectProperty

class TaskWidget(BoxLayout):
    task = ObjectProperty(None)
    tasks_list = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        checkbox = CheckBox(active=self.task['статус'])
        self.label = Label(text=self.task['описание'])
        self.add_widget(checkbox)
        self.add_widget(self.label)

class ToDoApp(App):
    def build(self):
        self.text_input = TextInput(font_size=30)
        button = Button(text='Добавить',  size_hint=(None, None), size=(100,50), background_color=(0.3,1,0.3,1))
        button.on_press = self.add_task
        self.layout = BoxLayout(size_hint=(0.9, None),  height=50, pos_hint={'center_x':0.5, 'top': 0.95},)
        self.layout.add_widget(self.text_input)
        self.layout.add_widget(button)

        return self.layout
    
    def add_task(self):
        text = self.text_input.text.strip()
        if text:
            task = {'описание':text, 'статус': False}
            task_widget = TaskWidget(task=task)
            self.layout.add_widget(task_widget)

app = ToDoApp()
app.run()
