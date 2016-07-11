import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.label import Label

for i in range(5):
    print __name__

class HelloApp(App):

    def build(self):
        return Label(text='Hello World')

if __name__ == '__main__':
    HelloApp().run()

print "___________________________"
print __name__
