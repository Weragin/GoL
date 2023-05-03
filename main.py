import tkinter as tk
import back_end

width = back_end.width
height = back_end.height
off = True


def update():
    global width, height, canvas
    back_end.next_generation()
    matrix = back_end.matrix
    for x in range(width):
        for y in range(height):
            overlap = canvas.find_overlapping(24*x+12, 24*y+12, 24*x+13, 24*y+13)
            for i in overlap:
                canvas.itemconfig(i, fill="black" * (back_end.matrix[x, y] == 1) + "white" * (
                            back_end.matrix[x, y] == 0))


def start():
    global off
    off = False
    button_run.config(text="Stop the simulation", command=stop)
    run()


def stop():
    global off
    off = True
    button_run.config(text="Run the simulation", command=start)


def run():
    global off
    update()
    if off:
        return
    canvas.after(500, run)


# button_run = tk.Button(window, text="Run the simulation", command=run)

window = tk.Tk()
window.title("John Conway's Game of Life")
window.geometry(f"{width*24 + 5}x{height*24+70}")
canvas = tk.Canvas(window, width=width*24 + 5, height=height*24+5)
canvas.grid(row=0, column=0, sticky="NW", rowspan=width, columnspan=height)


for x in range(width):
    x1 = x * 24 + 2
    x2 = x * 24 + 26
    for y in range(height):
        y1 = y * 24 + 2
        y2 = y * 24 + 26
        fill = "black" * (back_end.matrix[x, y] == 1) + "white" * (back_end.matrix[x, y] == 0)
        canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline="black")

button_step = tk.Button(window, text="Next Step", command=update)
button_step.grid(row=height + 1, column=1, sticky="NW")

button_run = tk.Button(window, text="Run the simulation", command=start) #back_end.turnOnOf
button_run.grid(row=height + 1, column=width - 2, sticky="NE")

tk.mainloop()
