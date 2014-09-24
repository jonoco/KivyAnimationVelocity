'''
fixed velocity animation
================

This is an example of using fixed velocity to animate a button across variable distances.
'''

import kivy
kivy.require('1.8.0')

from kivy.animation import Animation
from kivy.app import App
from kivy.uix.button import Button
from kivy.vector import Vector
from kivy.uix.boxlayout import BoxLayout

class Box(BoxLayout):
    
    def __init__(self, **kwargs):
        super(Box, self).__init__(**kwargs)
        # create a button and add it to the layout
        
        self.button = Button(text='zoom zoom!', size_hint=(None, None), size=(100,50), pos=self.pos)
        self.add_widget(self.button)
    
    def on_touch_down(self, value):
        # touch will to choose location to move button
        
        x = value.pos[0]
        y = value.pos[1]
        self.animate(x, y)
        
    def animate(self, x, y):
        # create an animation object and choose a velocity 
        
        velocity = 200  # 200 pixels per second
        
        x_start = self.button.x
        y_start = self.button.y
        
        x_end = x
        y_end = y
        
        distance = Vector(x_end, y_end).distance((x_start, y_start)) # absolute distance between button pos and touch pos
        duration = distance / velocity # algebraic!
        
        animation = Animation(x = x_end, y = y_end, d = duration)
        animation.start(self.button)
        
class VelocityApp(App):

    def build(self):    
        return Box()

if __name__ == '__main__':
    VelocityApp().run()
