import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frm = ttk.Frame(root, padding=10)
# frm.grid()
frm.pack(fill=tk.BOTH, expand=True)

label = ttk.Label(master=frm, text="Hello World", anchor="center") #.grid(column=0, row=0)
text = tk.Text(master=frm)

btn_frm = ttk.Frame(master=frm)
button = ttk.Button(master=btn_frm, text="Quit", command=root.destroy) #.grid(column=2, row=0)

label.pack(fill=tk.BOTH)
text.pack(fill=tk.BOTH, side=tk.LEFT)
btn_frm.pack(fill=tk.BOTH)

button.pack(padx=5)

root.resizable(width=False, height=False)

root.mainloop()