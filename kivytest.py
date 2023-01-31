import tkinter as tk
from tkVideoPlayer import TkinterVideo

class ScreenOne(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)
        self.config(bg='black')

        self.videoplayer = TkinterVideo(master=self, scaled=True)
        self.videoplayer.load(r"gifs/robot-movement-1-bg_9NA8s5Jz.gif")
        self.videoplayer.pack(expand=True, fill="both")
       
        self.videoplayer.bind("<<Loaded>>", lambda _: self.after(100, self.videoplayer.play())) # play the video

        # Add gif
        self.gif = tk.PhotoImage(file='gifs/ring.gif')
        self.gif_label = tk.Label(self, image=self.gif)
        self.gif_label.place(x=133, y=827)

        # Add text "1"
        self.text_1 = tk.Label(self, text="1", font=("inter bold", 170), bg='black')
        self.text_1.place(x=298, y=946)

        # Add text "in motion"
        self.text_2 = tk.Label(self, text="in motion", font=("inter bold", 170), bg='black')
        self.text_2.place(x=570, y=921)

        self.videoplayer.bind("<Ended>", self.videoplayer.play())


class ScreenTwo(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)
        self.config(bg='black')

        self.videoplayer = TkinterVideo(master=self, scaled=True)
        self.videoplayer.load(r"videos/PROCESS_MONITORING_OK_BG.mp4")
        self.videoplayer.pack(expand=True, fill="both")

        self.videoplayer.bind("<<Loaded>>", lambda _: self.after(100, self.videoplayer.play()))

        # Add text "OK"
        self.text = tk.Label(self, text="OK", font=("inter bold", 170), bg='black')
        self.text.place(x=642, y=921)

        self.videoplayer.bind("<Ended>", self.videoplayer.play())

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1536x2048")
        self.config(bg='black')

        self.screen_one = ScreenOne(self)
        self.screen_two = ScreenTwo(self)

        self.switch_to_screen_one()
        
        self.bind("1", self.switch_to_screen_one)
        self.bind("2", self.switch_to_screen_two)

        
    def switch_to_screen_one(self, *args):
        self.screen_two.pack_forget()
        self.screen_one.pack(fill="both", expand=True)
        self.screen_one.videoplayer.play()

    def switch_to_screen_two(self, *args):
        self.screen_one.pack_forget()
        self.screen_two.pack(fill="both", expand=True)
        self.screen_two.videoplayer.play()

if __name__ == '__main__':
    app = App()
    app.mainloop()