from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)

class TaskWidget(BoxLayout):
    def __init__(self, **data):
        super().__init__()
        self.size_hint_y = None
        self.height = 50

        checkbox = CheckBox(size_hint=(0.1, 1))
        self.label = Label(text='здесь будет ваша задача', color=(0,0,0,1), font_size=30)
        delete_button = Button(text='Удалить', size_hint=(0.33, 1),
        background_color=(1, 0.5, 0.5, 1), font_size=30)

        self.add_widget(checkbox)
        self.add_widget(self.label)
        self.add_widget(delete_button)

class ToDoApp(App):
    def build(self):
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
            task_widget = TaskWidget()
            self.tasks_layout.add_widget(task_widget)
    
app = ToDoApp()
app.run()

