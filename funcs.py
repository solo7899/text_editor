import tkinter as tk
from tkinter import filedialog

def save_file(text, label):
    """this fucntion is responsible for savedialago and file saving

    Args:
        text (tk.text|tk.Entry): textInput
    """
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("text file", "*.txt"), ("all files", "*.*")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                text_content = text.get("1.0", tk.END)
                file.write(text_content)
                label["text"] = file_path.split("/")[-1]
        except Exception as e:
            print(f"Error saving file {str(e)}")


def open_file(text, label):
    file_path = filedialog.askopenfilename(filetypes=(["text files", "*.txt"], ["all files", "*.*"]))
    if file_path:
        try:
            with open(file_path, "r") as file:
                file_context = file.read()
                text.insert("1.0", file_context)
                label["text"] = file_path.split("/")[-1]
        except Exception as e:
            print(f"Error reading file {0}", str(e))