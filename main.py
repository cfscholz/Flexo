import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x100")
        self.configure(bg="black")
        self.bind("1", self.screen1)
        self.bind("2", self.screen2)
        self.bind("3", self.screen3)
        self.bind("4", self.screen4)
        self.bind("5", self.screen5)
        self.bind("6", self.screen6)
        self.screen = None
        
    def screen1(self, event=None):
        if self.screen:
            self.screen.destroy()
        self.screen = tk.Canvas(self, bg="black", width=768, height=1024)
        self.screen.pack()
        self.screen.create_text(149, 473, text="1", font=("Inter-Bold", 85), fill="white")
        self.screen.create_text(321, 460, text="in motion", font=("Inter-Bold", 85), fill="white")
        
    def screen2(self, event=None):
        if self.screen:
            self.screen.destroy()
        self.screen = tk.Canvas(self, bg="black", width=768, height=1024)
        self.screen.pack()
        self.screen.create_text(321, 460, text="OK", font=("Inter-Bold", 85), fill="white")
    
    def screen3(self, event=None):
        if self.screen:
            self.screen.destroy()

    def screen4(self, event=None):
        if self.screen:
            self.screen.destroy()
    
    def screen5(self, event=None):
        if self.screen:
            self.screen.destroy()

    def screen6(self, event=None):
        if self.screen:
            self.screen.destroy()
        
if __name__ == '__main__':
    app = App()
    app.mainloop()
