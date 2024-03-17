import tkinter as tk
from tkinter import filedialog

from sort import sort_photos


def photos_app():
    # Make a simple GUI application that sorts photos

    # Step 1 - Create a window
    window = tk.Tk()

    # Handlers for events
    def handle_select(event):
        window.folder = filedialog.askdirectory()

    def handle_sort(event):
        sort_photos(window.folder)

    # Step 2 - Add a label to the window
    select_label = tk.Label(text="Select a folder with photos:")
    select_label.pack()

    # Step 3 - Add a button to the window
    select_button = tk.Button(window, text="Select folder")
    select_button.bind("<Button-1>", handle_select)  # <Button-1> is the left mouse button click event
    select_button.pack()

    # Step 4 - Add another label to the window
    sort_label = tk.Label(text="Sort photos")
    sort_label.pack()

    # Step 5 - Add another button to the window
    sort_button = tk.Button(window, text="Sort photos")
    sort_button.bind("<Button-1>", handle_sort)  # <Button-1> is the left mouse button
    sort_button.pack()

    # Step 6 - Start the tkinter main loop
    window.mainloop()
