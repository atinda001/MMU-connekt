from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup

class HomePage(FloatLayout):
    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)
        self.top_bar = BoxLayout(size_hint=(1, 0.1), pos_hint={'top': 1})
        self.top_bar.add_widget(Label(text='Twitter', font_size=20))
        self.edit_profile = Button(text='Edit Profile', size_hint_x=None, width=150)
        self.edit_profile.bind(on_press=self.open_edit_profile)
        self.top_bar.add_widget(self.edit_profile)
        self.add_widget(self.top_bar)

        self.bottom_bar = BoxLayout(size_hint=(1, 0.1), pos_hint={'bottom': 1}, orientation='horizontal')
        self.home = Button(text='Home', size_hint_x=None, width=150)
        self.home.bind(on_press=self.open_home)
        self.group = Button(text='Group', size_hint_x=None, width=150)
        self.group.bind(on_press=self.open_group)
        self.chat.bind(on_press=self.open_chat)
        self.bottom_bar.add_widget(self.home)
        self.bottom_bar.add_widget(self.group)
        self.bottom_bar.add_widget(self.chat)
        self.add_widget(self.bottom_bar)

        # add icons to buttons
        self.home.add_widget(Image(source='home_icon.png', size_hint=(None, None), size=(20, 20)))
        self.group.add_widget(Image(source='group_icon.png', size_hint=(None, None), size=(20, 20)))
        self.chat.add_widget(Image(source='chat_icon.png', size_hint=(None)))


    def open_edit_profile(self, instance):
        content = Label(text='This is your profile')
        self.popup = Popup(title='Edit Profile', content=content, size_hint=(0.7, 0.7))
        self.popup.open()

    def open_home(self, instance):
        print("Open Home")

    def open_group(self, instance):
        print("Open Group")
        
    def open_chat(self, instance):
        print("Open Chat")


from kivy.uix.screenmanager import ScreenManager, Screen

class HomeScreen(Screen):
    pass

class GroupScreen(Screen):
    pass

class ChatScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.home_screen = HomeScreen(name='home')
        self.screen_manager.add_widget(self.home_screen)

        self.group_screen = GroupScreen(name='group')
        self.screen_manager.add_widget(self.group_screen)

        self.chat_screen = ChatScreen(name='chat')
        self.screen_manager.add_widget(self.chat_screen)

        return self.screen_manager

if __name__ == '__main__':
    MyApp().run()

