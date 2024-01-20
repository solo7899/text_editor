import tkinter as tk
from tkinter import filedialog

file_path = ""

def enable_button(button):
    if file_path:
        button["state"] = tk.NORMAL

def save_file(text, label, button):
    """
    this fucntion is responsible for savedialago and file saving

    Args:
        text (tk.text|tk.Entry): textInput
        label (tk.label|ttk.label) : Label
    """
    global file_path
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("text file", "*.txt"), ("all files", "*.*")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                text_content = text.get("1.0", tk.END)
                file.write(text_content)
                label["text"] = file_path.split("/")[-1]
                enable_button(button)
        except Exception as e:
            print(f"Error saving file {str(e)}")


def open_file(text, label, button):
    """
    this fucntion is responsible for opendialago and file file opening

    Args:
        text (tk.text|tk.Entry): textInput
        label (tk.label|ttk.label) : Label
    """
    global file_path
    file_path = filedialog.askopenfilename(filetypes=(["text files", "*.txt"], ["all files", "*.*"]))
    if file_path:
        try:
            with open(file_path, "r") as file:
                file_context = file.read()
                text.delete("1.0", tk.END)
                text.insert("1.0", file_context)
                label["text"] = file_path.split("/")[-1]
                enable_button(button)
                print(button["state"])
        except Exception as e:
            print(f"Error reading file {0}", str(e))

            
def quick_save(text):
    if file_path:
        try:
            with open(file_path, "w") as file:
                file_content = text.get("1.0", tk.END)
                file.write(file_content)
        except Exception as e:
            print(f"Error {0}", str(e))

