from tkinter import *
from tkvideo import tkvideo

root = Tk()
my_label = Label(root)
my_label.pack()
player = tkvideo("videos/ROBOT_MOVEMENT_1_BG.mp4", my_label, loop = 1, size = (1280,720))
player.play()

root.mainloop()