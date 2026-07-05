
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

class GalaryScreen(Screen):
    pass

class GalaryScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

class HomeScreen(Screen):
    # Clock.schedule_once(lambda dt: self.ids.nav_drawer.set_state("closed"), 0.5)
    def say_hello(self):
        output = "Hi there! Welcome to KivyMD!"
        self.ids.greeting.text = output

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Light"
        
        root = Builder.load_file("screens/main.kv")
        # Clock.schedule_once(lambda dt: root.ids.nav_drawer.set_state("closed"), 0.5)
        
        return root


MyApp().run()