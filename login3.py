from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class LoginPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.size_hint = (0.5, 0.5)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.add_widget(Label(text='Username'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.submit = Button(text='Login', size_hint = (0.5,0.4))
        self.submit.bind(on_press=self.verify_info)
        self.add_widget(self.submit)
        
    def verify_info(self, instance):
        # Verify the information entered with the information used during signup
        pass

class LoginApp(App):
    def build(self):
        return LoginPage()

if __name__ == '__main__':
    LoginApp().run()

