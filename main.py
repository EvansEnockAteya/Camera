from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
MDScreen:

    MDBoxLayout:
        orientation: "vertical"
        padding: "30dp"
        spacing: "20dp"

        Widget:
            size_hint_y: .3

        MDLabel:
            id: greeting
            text: "Welcome!"
            halign: "center"
            font_style: "H6"
            adaptive_height: True

        MDRaisedButton:
            text: "Say Hello"
            pos_hint: {"center_x": .5}
            on_release: app.say_hello()

        Widget:
            size_hint_y: .4
'''


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def say_hello(self):
        self.root.ids.greeting.text = "Hi there! Welcome to KivyMD!"


MyApp().run()