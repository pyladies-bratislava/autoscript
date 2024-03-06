import tkinter as tk
from tkinter import filedialog

from sort import organize_pics


# Make a simple GUI application that organizes pictures by year/month according to the filename.
def photos_app():
    folder = None

    window = tk.Tk()

    def handle_click(event):
        window.folder = filedialog.askdirectory()

    # Chose a folder to organize
    label = tk.Label(text="Select a folder with photos:")
    label.pack()
    button1 = tk.Button(window, text="Select")
    button1.bind("<Button-1>", handle_click)
    button1.pack()

    button2 = tk.Button(window, text="Organize pictures", command=lambda: organize_pics(window.folder))
    button2.pack()

    window.mainloop()
