from kivymd.app import MDApp
from kivy.lang import Builder


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        return Builder.load_file("screens/main.kv")

    def say_hello(self):
        self.root.ids.greeting.text = "Hi there! Welcome to KivyMD!"


MyApp().run()