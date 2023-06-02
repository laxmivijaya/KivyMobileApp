from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Ellipse, Color

Window.clearcolor = (0,0,0,1)

class PaintWindow(Widget):
    def on_touch_down(self, touch):
        self.canvas.add(Color(rgb=(1,0,0)))
        d = 30
        self.canvas.add(Ellipse(pos=(touch.x, touch.y), size=(d,d)))

class PaintApp(App):
    def build(self):
        return PaintWindow()

PaintApp().run()


