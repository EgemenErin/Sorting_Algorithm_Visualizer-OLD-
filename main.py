import tkinter as tk
from tkinter import ttk
import random
from bubbleSort import bubble_sort

root = tk.Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900, 600)
root.config(bg='black')

# variables
selected_alg = tk.StringVar()
data = []

# function to draw the data on canvas
def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        # top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        # bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=tk.SW, text=str(data[i]))

    root.update_idletasks()

# function to generate data
def Generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = [random.randrange(minVal, maxVal + 1) for _ in range(size)]

    drawData(data, ['red' for x in range(len(data))])

# wrapper function to call bubble_sort with root.after
def StartAlgorithm():
    global data
    def callback():
        root.after(1, lambda: None)  # A no-op to keep the event loop running
    bubble_sort(data, drawData, speedScale.get(), callback)

# frame for user interface
UI_frame = tk.Frame(root, width=600, height=200, bg='purple')
UI_frame.grid(row=0, column=0, padx=10, pady=5)
canvas = tk.Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

# user interface elements
tk.Label(UI_frame, text="Algorithm: ", bg='purple').grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)
speedScale = tk.Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=tk.HORIZONTAL,
                   label="Select Speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)
tk.Button(UI_frame, text="Start", command=StartAlgorithm, bg='red').grid(row=0, column=3, padx=5, pady=5)
sizeEntry = tk.Scale(UI_frame, from_=3, to=25, resolution=1, orient=tk.HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)
minEntry = tk.Scale(UI_frame, from_=0, to=10, resolution=1, orient=tk.HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)
maxEntry = tk.Scale(UI_frame, from_=10, to=100, resolution=1, orient=tk.HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)
tk.Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()