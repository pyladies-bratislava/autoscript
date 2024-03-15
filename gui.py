import tkinter as tk
from tkinter import filedialog

from sort import sort_pics


def photos_app():
    # Make a simple GUI application that sorts pictures by year/month according to the filename.

    # Step 1 - Create a window
    window = tk.Tk()

    # TODO: check if this can go somewhere else
    def handle_click(event):
        window.folder = filedialog.askdirectory()

    # Step 2 - Add a label to the window
    label = tk.Label(text="Select a folder with photos:")
    label.pack()

    # Step 3 - Add a button to the window
    button1 = tk.Button(window, text="Select")
    button1.bind("<Button-1>", handle_click)
    button1.pack()

    # Step 4 - Add another label to the window
    label = tk.Label(text="Sort pictures!")
    label.pack()

    # Step 5 - Add another button to the window that calls our sort_pics function
    button2 = tk.Button(
        window, text="Sort photos", command=lambda: sort_pics(window.folder)
    )
    button2.pack()

    # Step 6 - Start the tkinter main loop
    window.mainloop()
