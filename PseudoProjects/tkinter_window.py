import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

# root = ThemedTk(theme="arc")
# root.title("Themed Tkinter Example")
# ttk.Label(root, text="Themed Tkinter").pack(pady=50)
# root.mainloop()

root = tk.Tk()
root.title("Tkinter Example")
root.geometry("300x200")

label = ttk.Label(root, text="Hello, Tkinter!")
label.pack(pady=50)

root.mainloop()
