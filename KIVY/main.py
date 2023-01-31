import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.video import Video
from kivy.uix.image import Image
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.animation import Animation

kivy.require('1.11.1')

LabelBase.register(name="Inter-Bold", fn_regular="Inter-Bold.otf")

class ScreenOne(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.video = Video(source='screen_one_video.mp4', state='play', loop=True)
        self.gif = Image(source='screen_one_gif.gif', pos=(133, 827), size=(393, 393), anim_delay=0.1)
        self.add_widget(self.video)
        self.add_widget(self.gif)
        self.text1 = kivy.uix.label.Label(text="1", pos=(298, 946), font_name="Inter-Bold", font_size=170)
        self.text2 = kivy.uix.label.Label(text="in motion", pos=(570, 921), font_name="Inter-Bold", font_size=170)
        self.add_widget(self.text1)
        self.add_widget(self.text2)
        
class ScreenTwo(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.video = Video(source='screen_two_video.mp4', state='play', loop=True)
        self.add_widget(self.video)
        self.text = kivy.uix.label.Label(text="OK", pos=(642, 921), font_name="Inter-Bold", font_size=170)
        self.add_widget(self.text)
        
class MainApp(App):
    def build(self):
        self.screen_one = ScreenOne()
        self.screen_two = ScreenTwo()
        Window.size = (1536, 2048)
        self.root = Widget()
        self.root.add_widget(self.screen_one)
        self.root.canvas.add(kivy.graphics.Rectangle(source='black.jpg', size=Window.size))
        Window.bind(on_key_down=self.key_input)
        return self.root
    
    def key_input(self, window, key, *args):
        if key == 49:  # key 1
            self.root.clear_widgets()
            self.root.add_widget(self.screen_one)
        if key == 50:  # key 2
            self.root.clear_widgets()
            self.root.add_widget(self.screen_two)
        
if __name__ == "__main__":
    MainApp().run()
