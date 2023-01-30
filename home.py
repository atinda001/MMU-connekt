from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')

        # Scrollable screen
        scroll_view = ScrollView()
        root.add_widget(scroll_view)

        # Box layout to hold post items
        post_box = BoxLayout(orientation='vertical', size_hint_y=None)
        post_box.bind(minimum_height=post_box.setter('height'))
        scroll_view.add_widget(post_box)

        # Text input for creating new posts
        post_input = TextInput(hint_text="Enter text or upload an image...")
        post_box.add_widget(post_input)

        # Icon for creating new posts
        post_icon = Button(text="+", size_hint_y=None, height=40)
        post_box.add_widget(post_icon)

        # Group and chat icons
        group_icon = Button(text="Group", size_hint_y=None, height=40)
        root.add_widget(group_icon)

        chat_icon = Button(text="Chat", size_hint_y=None, height=40)
        root.add_widget(chat_icon)

        return root

if __name__ == '__main__':
    MyApp().run()

