import sys
import tkinter
from tkinter import ttk
from tkinter.tix import *

class Post_It:
    text = ''
    pinned = False
    order = None

class Notes:
    post_its = []
    text_grid = []
    root = None

    def __init__(self):
        root = tkinter.Tk("Post Its")
        frame = Frame(width="500",height="500")
        frame.pack()
        swin = ScrolledWindow(frame, width=500, height=500)
        swin.pack()
        win = swin.window
        for x in range(0, 3):
            self.text_grid.append(tkinter.Text(self.root))
        for y in range(0, 3):
            self.text_grid[y].grid()
        root.mainloop()

def main():
    notes = Notes()

if __name__ == "__main__":
    main()
