import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Calculator (built in python)")
root.geometry("400x400")

operation = tk.Label(
    root,
    text="test operation",
    background="lightblue",
    height=2
)

operation.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)

for row in range(1, 5):
    for col in range(5):
        operation_btn = tk.Button(
            root, text="x"
        )
        operation_btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

for col in range(5):
    root.grid_columnconfigure(col, weight=1)
for row in range(5):
    root.grid_rowconfigure(row, weight=1)
root.mainloop()
