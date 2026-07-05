
from kivymd.app import MDApp
from kivy.lang import Builder

from kivy.clock import Clock

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Light"
        
        root = Builder.load_file("screens/main.kv")
        Clock.schedule_once(lambda dt: root.ids.nav_drawer.set_state("closed"), 0.5)
        
        return root

    def say_hello(self):
        output = "Hi there! Welcome to KivyMD!"
        self.root.ids.greeting.text = output


MyApp().run()