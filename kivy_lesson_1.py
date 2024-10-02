from kivy.app import App
from kivy.uix.button import Button 
from kivy.uix.label import Label 
from kivy.uix.boxlayout import BoxLayout 

class MyApp(App):
   def build(self):

      txt = Label(text='Это надпись') 
      btn = Button(text='Это кнопка')
      layout = BoxLayout()
      layout.add_widget(txt)
      layout.add_widget(btn)
      return layout 

MyApp().run()
