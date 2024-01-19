import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frm = ttk.Frame(root, padding=10)
# frm.grid()
frm.pack()

label = ttk.Label(master=frm, text="Hello World") #.grid(column=0, row=0)
text = tk.Text(master=frm)
button = ttk.Button(master=frm, text="Quit", command=root.destroy) #.grid(column=2, row=0)

label.pack()
text.pack(fill=tk.X)
button.pack()

root.mainloop()