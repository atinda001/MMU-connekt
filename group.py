# main.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CreateGroupPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"

        self.group_name_input = TextInput(hint_text="Group Name")
        self.add_widget(self.group_name_input)

        self.group_desc_input = TextInput(hint_text="Group Description")
        self.add_widget(self.group_desc_input)

        self.submit_button = Button(text="Submit", on_press=self.submit)
        self.add_widget(self.submit_button)

    def submit(self, instance):
        group_name = self.group_name_input.text
        group_desc = self.group_desc_input.text

        # Store the group data in a data structure or save to a database here

        # Reset the input fields
        self.group_name_input.text = ""
        self.group_desc_input.text = ""

class MyApp(App):
    def build(self):
        return CreateGroupPage()

if __name__ == "__main__":
    MyApp().run()

