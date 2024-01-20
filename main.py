import tkinter as tk 
from tkinter import ttk, font

root = tk.Tk()
frm = ttk.Frame(root, padding=10)
# frm.grid()
frm.pack(fill="both" ,side="top", expand=True)

fontObj = font.Font(size=18)

label = ttk.Label(master=frm, text="Hello World", anchor="center") #.grid(column=0, row=0)
text = tk.Text(master=frm, font=fontObj)

btn_frm = ttk.Frame(master=frm)
Q_button = ttk.Button(master=btn_frm, text="Quit", command=root.destroy) #.grid(column=2, row=0)
S_button = ttk.Button(master=btn_frm, text="Save") #.grid(column=2, row=0)


label.pack(fill="both")
text.pack(fill="both", side="top", expand=True)

# btn_frm.rowconfigure(0, weight=1, minsize=25)
# btn_frm.columnconfigure(0, weight=1, minsize=25)

btn_frm.pack(fill="both", side="top", expand=True)
Q_button.grid(padx=5, pady=5, sticky="w", column=0, row=0)
S_button.grid(column=1, row=0, padx=5, pady=5)


root.resizable(width=False, height=False)

root.mainloop()