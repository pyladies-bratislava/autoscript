import tkinter as tk
from tkinter import filedialog

from sort import organize_pics


# Make a simple GUI application that organizes pictures by year/month according to the filename.
def photos_app():
    window = tk.Tk()
    window.title("Sort pictures")
    window.geometry("400x300")

    def handle_click(event):
        window.folder = filedialog.askdirectory()

    # Chose a folder to organize
    label = tk.Label(text="Select a folder with photos:")
    label.pack(side="left")
    button1 = tk.Button(window, text="Select", width=15, height=2)
    button1.bind("<Button-1>", handle_click)
    button1.pack(side="right", padx=2)

    label = tk.Label(text="Organize pictures!")
    label.pack(side="right", padx=1)
    button2 = tk.Button(
        window,
        text="Click here to organize pictures",
        width=25,
        height=2,
        command=lambda: organize_pics(window.folder),
    )
    button2.pack(side="left", padx=2)

    window.mainloop()
