from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color

class SignupPage(RelativeLayout):
    def __init__(self, **kwargs):
        super(SignupPage, self).__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 1)
        self.grid = GridLayout(cols=2, size_hint=(0.8, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.grid.add_widget(Label(text='Email'))
        self.email = TextInput(multiline=False)
        self.grid.add_widget(self.email)
        self.grid.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        self.grid.add_widget(self.password)
        self.signup = Button(text='Sign Up', size_hint_x=None, width=150, pos_hint={'center_x': 0.5})
        self.grid.add_widget(self.signup)
        self.signup.bind(on_press=self.submit)
        self.add_widget(self.grid)
        self.google = Button(text="Signup with google", size_hint_y=None, height=30, pos_hint={'center_x': 0.5, 'y': 0})
        self.add_widget(self.google)
        self.google.bind(on_press = self.google_signup)

    def google_signup(self, instance):
        # code to submit the google signup
        print("Google Signup")
        
    def submit(self, instance):
        email = self.email.text
        password = self.password.text
        # code to submit the email and password to the server
        print(f"email is {email} and password is {password}")
        
class MyApp(App):
    def build(self):
        return SignupPage()

if __name__ == '__main__':
    MyApp().run()

