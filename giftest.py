import tkinter as tk
from PIL import Image, ImageTk

# Load the gif
gif = Image.open("gifs/ring.gif")

# Create a class to hold the gif frames
class GIF_APP:
    def __init__(self):
        self.gif_frames = []
        for i in range(gif.n_frames):
            gif.seek(i)
            gif_frame = gif.copy()
            gif_frame.load()
            gif_frame = ImageTk.PhotoImage(gif_frame)
            self.gif_frames.append(gif_frame)


root = tk.Tk()
gif_app = GIF_APP()
root.title("GIF Example")

# Create a label to display the gif
label = tk.Label(root, image=gif_app.gif_frames[0])
label.pack()

# Function to update the gif frame
def update_gif(gif_frame):
    label.config(image=gif_frame)
    root.after(100, update_gif, gif_app.gif_frames[(gif_app.gif_frames.index(gif_frame)+1)%len(gif_app.gif_frames)])

# Start the gif animation
root.after(0, update_gif, gif_app.gif_frames[0])
root.mainloop()