
from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
Screen:

    MDBoxLayout:
        orientation: "vertical"
        padding: "20dp"
        spacing: "15dp"

        Widget:
            size_hint_y: .3

        MDLabel:
            id: label
            text: "Welcome"
            adaptive_height: True
            font_style: "H4"
                       

        MDFlatButton:
            text: "Click me!!"
            size_hint_y: None
            pos_hint: {"center_x": .5}
            on_release: app.say_hello()

        Widget:
            size_hint_y: .4
'''

class MyApp(MDApp):
    def build(self):
        root = Builder.load_string(KV)
        return root
    
    def say_hello(self):
        output = "Hello there"
        self.root.ids.label.text = output
    
MyApp().run()
