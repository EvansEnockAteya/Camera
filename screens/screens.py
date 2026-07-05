
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen

class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Supplier(Contact):
    def order(self, item):
        return f"Order for {item} from {self.name} : {self.email}"
    
class ContactManager:
    def __init__(self):
        self.suppliers = []

    def add_supplier(self, name, email):
        self.suppliers.append(Supplier(name, email))

    def get_supplier_names(self):
        return [supplier.name for supplier in self.suppliers]
    
    def get_supplier(self, name):
        for supplier in self.suppliers:
            if supplier.name == name:
                return supplier
            return None
        
    def get_all_suppliers_text(self):
        if not self.suppliers:
            return "No suppliers found"
        return "\n".join(
            f"{supplier.name} - {supplier.email}"
            for supplier in self.suppliers
        )
    
KV = '''
ScreenManager:
    MenuScreen:
    AddSupplierScreen:
    ContactsScreen:
    OrderScreen:

<MenuScreen>:
    name: "menu"

    BoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(15)

        Label:
            text: "Supplier Manager"
            font_size: sp(28)
        
        Button:
            text: "Add Supplier"
            on_release: app.root.current = "add"

        Button:
            text: "View Suppliers"
            on_release: root.manager.current = "contacts"

        Button:
            text: "Place Order"
            on_release: root.manager.current = "order"

<AddSupplierScreen>:
    name: "add"

    BoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(15)

        Label:
            text: "Add Supplier"
            font_size: sp(24)

        TextInput:
            id: name_input
            hint_text: "Supplier name"
            multiline: False
            size_hint_y: None
            height: dp(45)
        
        TextInput:
            id: email_input
            hint_text: "Supplier email"
            multiline: False
            size_hint_y: None
            height: dp(45)

        Button:
            text: "Save"
            on_release: root.save_supplier()

        Label:
            text: root.message
            text_size: self.size

        Widget:

        Button:
            text: "Back"
            size_hint_y: None
            height: dp(50)
            on_release: root.manager.current = "menu"

<ContactsScreen>:
    name: "contacts"

    BoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(15)

        Label:
            text: "Suppliers"
            font_size: sp(24)
            size_hint_y: None
            height: dp(50)

        ScrollView:
            Label:
                text: root.contacts_text
                text_size: self.width, None
                size_hint_y: None
                height: max(self.texture_size[1], self.parent.height)

        Button:
            text: "Back"
            size_hint_y: None
            height: dp(50)
            on_release: root.manager.current = "menu"

<OrderScreen>:
    name: "order"

    BoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(15)

        Label:
            text: "Place order"
            font_size: sp(24)

        Spinner:
            id: supplier_spinner
            text: "Select Supplier"
            values: root.supplier_names

        TextInput:
            id: item_input
            hint_text: "Order item"
            multiline: False
            size_hint_y: None
            heighe: dp(45)

        Button:
            text: "Submit order"
            on_release: root.place_order()

        Label: 
            text: root.message
            text_size: self.size

        Widget:

        Button:
            text: "Back"
            size_hint_y: None
            height: dp(50)
            on_release: root.manager.current = "menu"

'''

class MenuScreen(Screen):
    pass


class AddSupplierScreen(Screen):
    message = StringProperty("")

    def save_supplier(self):
        name = self.ids.name_input.text.strip()
        email = self.ids.email_input.text.strip()

        if not name:
            self.message = "Enter supplier name.."
            return
        if not email:
            self.message = "Enter supplier email."
            return
        
        app = App.get_running_app()
        app.contact_manager.add_supplier(name, email)

        self.ids.name_input.text = ""
        self.ids.email_input.text = ""

        self.status = f"{name} added."

        def on_pre_enter(self):
            self.message = ""


class ContactsScreen(Screen):
    contacts_text = StringProperty("")

    def on_pre_enter(self):
        app = App.get_running_app()
        self.contacts_text = app.contact_manager.get_all_suppliers_text()


class OrderScreen(Screen):
    supplier_names = ListProperty([])
    message = StringProperty("")

    def on_pre_enter(self):
        app = App.get_running_app()

        self.supplier_names = app.contact_manager.get_supplier_names()
        self.ids.supplier_spinner.text = "Select supplier"
        self.ids.item_input.text = ""
        self.message = ""

    def place_order(self):
        supplier_name = self.ids.supplier_spinner.text
        item = self.ids.item_input.text.strip()

        if supplier_name == "Select supplier":
            self.message = "Choose a supplier"
            return
        
        if not item:
            self.status = "Enter an item"
            return
        
        app = App.get_running_app()
        supplier = app.contact_manager.get_supplier(supplier_name)

        if supplier is None:
            self.message = "Supplier not found."
            return
        
        self.message = supplier.order(item)



class SupplierApp(App):
    def build(self):
        self.contact_manager = ContactManager()

        self.contact_manager.add_supplier("Evans Enock", "evans@gmail.com")
        self.contact_manager.add_supplier("Elvis Kruger", "elvis@gmail.com")

        return Builder.load_string(KV)
    
SupplierApp().run()
