import tkinter as tk 
from tkinter import ttk, font
import sys

from funcs import save_file, open_file, quick_save 

#makeing the main window
main_window = tk.Tk()
main_window.bind("<Escape>" , sys.exit)

#setting the main Frame
frm = ttk.Frame(main_window, padding=10)
# frm.grid()
frm.pack(fill="both" ,side="top", expand=True)

#setting main Frame objects
fontObj = font.Font(size=18)
label = ttk.Label(master=frm, text="", anchor="center") #.grid(column=0, row=0)
text = tk.Text(master=frm, font=fontObj)

#setting btnFrame and its objects
btn_frm = ttk.Frame(master=frm)
Q_button = ttk.Button(master=btn_frm, text="Quit", command=main_window.destroy) #.grid(column=2, row=0)
S_button = ttk.Button(master=btn_frm, text="Save", command=lambda: save_file(text, label, Qs_button)) #.grid(column=2, row=0)
O_button = ttk.Button(master=btn_frm, text="Open", command=lambda: open_file(text, label, Qs_button))
Qs_button = ttk.Button(master=btn_frm, text="Quick Save",  state=tk.DISABLED, command=lambda: quick_save(text))

label.pack(fill="both")
text.pack(fill="both", side="top", expand=True)
text.focus()

# btn_frm.rowconfigure(0, weight=1, minsize=25)
# btn_frm.columnconfigure(0, weight=1, minsize=25)

btn_frm.pack(fill="both", side="top", expand=True)
Q_button.grid(padx=5, pady=5, sticky="w", column=0, row=0)
S_button.grid(column=1, row=0, padx=5, pady=5)
O_button.grid(column=2, row=0, padx=5, pady=5)
Qs_button.grid(column=3, row=0, padx=5, pady=5)


main_window.resizable(width=False, height=False)

main_window.mainloop()