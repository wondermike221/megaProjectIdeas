"""Text Editor V 0.0.1 Alpha"""
import sys
import tkinter as tk
from tkinter import filedialog

V = sys.version

ROOT = tk.Tk("Text Editor")
TEXT = tk.Text(ROOT)
TEXT.grid()
def save_as():
    """Saves text"""
    global TEXT
    the_text = TEXT.get("1.0", "end-1c")
    save_location = filedialog.asksaveasfilename()
    file1 = open(save_location, "w+")
    file1.write(the_text)
    file1.close()

BUTTON = tk.Button(ROOT, text="Save", command=save_as)
BUTTON.grid()

ROOT.mainloop()
