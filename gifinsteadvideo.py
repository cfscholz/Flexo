import tkinter as tk

class ScreenOne(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)
        self.config(bg='black')

        # Add gif
        self.gif = tk.PhotoImage(file='gifs/robot-movement-1-bg_9NA8s5Jz.gif')
        self.gif_label = tk.Label(self, image=self.gif)
        self.gif_label.pack(expand=True, fill="both")
       
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


class ScreenTwo(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)
        self.config(bg='black')

        # Add gif
        self.gif = tk.PhotoImage(file='gifs/process-monitoring-ok-bg_T5OhKvWV.gif')
        self.gif_label = tk.Label(self, image=self.gif)
        self.gif_label.pack(expand=True, fill="both")

        # Add text "OK"
        self.text = tk.Label(self, text="OK", font=("inter bold", 170))
        self.text.place(x=100, y=100)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1536x2048")
        self.config(bg='black')

        self.screen_one = ScreenOne(self)
        self.screen_two = ScreenTwo(self)

        
        
        self.bind("1", self.switch_to_screen_one)
        self.bind("2", self.switch_to_screen_two)

        self.switch_to_screen_one()

        
    def switch_to_screen_one(self, *args):
        self.screen_two.pack_forget()
        self.screen_one.pack(fill="both", expand=True)

    def switch_to_screen_two(self, *args):
        self.screen_one.pack_forget()
        self.screen_two.pack(fill="both", expand=True)

if __name__ == '__main__':
    app = App()
    app.mainloop()
