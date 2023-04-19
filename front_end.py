import tkinter as tk
import numpy


def setup(height, width, state):
    window = tk.Tk()
    window.title("John Conway's Game of Life")
    window.geometry(f"{width*24 + 5}x{height*24+52}")
    canvas = tk.Canvas(window)
    canvas.pack()
    for x in range(width):
        for y in range(height):
            x1 = x * 24 + 2
            y1 = y * 24 + 2
            x2 = x * 24 + 26
            y2 = y * 24 + 26
            canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")

    button = tk.Button(window, text="Next Step", command=lambda: print("GO!"))
    button.pack()

    tk.mainloop()
