import tkinter as tk
from tkinter import ttk

def convert():
    output_string.set(entry_int.get())


#window
window = tk.Tk()
window.title("Demo")
window.geometry("300x150")

#title
title_label = ttk.Label(master = window, text = "Covert this to this", font = "Calibri 24")
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = "Convert", command = convert)
entry.pack(side = "left", padx = 10)
button.pack(side = "left", pady = 10)
input_frame.pack()


#output 
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = "Calibri 24", textvariable = output_string)
output_label.pack()


#run
window.mainloop()
