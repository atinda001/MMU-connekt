from kivy.app import App
from kivy.uix.image import AsyncImage

class MyApp(App):
	def build(self):
		return AsyncImage(source = 'https://beraportal.com/ke/wp-content/uploads/sites/2/2019/09/Multimedia-University.png ')

if __name__ == '__main__':
	MyApp().run()
