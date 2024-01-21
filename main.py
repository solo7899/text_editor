import tkinter as tk 
from tkinter import ttk, font
import sys

from funcs import save_as_file, open_file, save

#makeing the main window
main_window = tk.Tk()
main_window.bind("<Escape>" , sys.exit)

#setting menu
menu_bar =  tk.Menu(main_window, background="grey")

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=lambda:open_file(text, label, file_menu))
file_menu.add_command(label="Save as", command=lambda:save_as_file(text, label, file_menu))
file_menu.add_command(label="Save", command=lambda:save(text), state=tk.DISABLED)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=main_window.destroy)

menu_bar.add_cascade(label="File", menu=file_menu)

#setting the main Frame
frm = ttk.Frame(main_window)
# frm.grid()
frm.pack(fill="both" ,side="top", expand=True)

#setting main Frame objects
fontObj = font.Font(size=18)
label = ttk.Label(master=frm, text="", anchor="center") #.grid(column=0, row=0)
text = tk.Text(master=frm, font=fontObj)

# #setting btnFrame and its objects
# btn_frm = ttk.Frame(master=frm)
# Q_button = ttk.Button(master=btn_frm, text="Quit", command=main_window.destroy) #.grid(column=2, row=0)
# save_as_button = ttk.Button(master=btn_frm, text="Save as", command=lambda: save_as_file(text, label, save_button)) #.grid(column=2, row=0)
# open_button = ttk.Button(master=btn_frm, text="Open", command=lambda: open_file(text, label, save_button))
# save_button = ttk.Button(master=btn_frm, text="Save",  state=tk.DISABLED, command=lambda: save(text))

label.pack(fill="both")
text.pack(fill="both", side="top", expand=True)
text.focus()

# btn_frm.rowconfigure(0, weight=1, minsize=25)
# btn_frm.columnconfigure(0, weight=1, minsize=25)

# btn_frm.pack(fill="both", side="top", expand=True)
# Q_button.grid(padx=5, pady=5, sticky="w", column=0, row=0)
# save_as_button.grid(column=1, row=0, padx=5, pady=5)
# open_button.grid(column=2, row=0, padx=5, pady=5)
# save_button.grid(column=3, row=0, padx=5, pady=5)


main_window.resizable(width=False, height=False)
main_window.config(menu=menu_bar)

main_window.mainloop()