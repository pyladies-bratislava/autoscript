import tkinter as tk
from tkinter import filedialog

from sort import sort_pics


# Make a simple GUI application that sorts pictures by year/month according to the filename.
def photos_app():
    window = tk.Tk()

    def handle_click(event):
        window.folder = filedialog.askdirectory()

    # Chose a folder to organize
    label = tk.Label(text="Select a folder with photos:")
    label.pack()
    button1 = tk.Button(
        window,
        text="Select",
    )
    button1.bind("<Button-1>", handle_click)
    button1.pack()

    # Sort pictures
    label = tk.Label(text="Sort pictures!")
    label.pack()
    button2 = tk.Button(
        window,
        text="Click here to sort pictures",
        command=lambda: sort_pics(window.folder),
    )
    button2.pack()

    window.mainloop()
