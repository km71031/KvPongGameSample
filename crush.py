from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

class Escape(Widget):
    p1 = ObjectProperty(None)
    enemy = []
    for i in range(20):
        enemy.append(ObjectProperty(None))

    #def start(self, player):
    p1.center = (3, 3)



