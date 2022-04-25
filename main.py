from tkinter import *
import settings
root = Tk();
#Override the settings of the window
root.configure(bg = "black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('minesweeper')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg = "red",
    width = 1000,
    height = 200
)

top_frame.place(x = 0, y = 0)

left_frame  = Frame(
    root,
    bg = "blue",
    width = 200,
    height = 600
)

left_frame.place(x = 0, y = 200)

#Run the window
root.mainloop()