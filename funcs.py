import tkinter as tk
from tkinter import filedialog

def save_file(text):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("text file", "*.txt"), ("all files", "*.*")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                text_content = text.get("1.0", tk.END)
                file.write(text_content)
        except Exception as e:
            print(f"Error saving file {str(e)}")

