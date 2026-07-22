import tkinter as tk
from tkinter import ttk


root = tk.Tk()

root.title("Calculator (built in python)")
root.geometry("400x400")    

button_names = [
    "9", "8", "7", "CE", "xʸ",
    "6", "5", "4", "-", "ʸ√x",
    "3", "2", "1", "+", "x",
    "0", ".", "C", "Exe", "/"
]

display_text = tk.StringVar()
display_text.set("0")

operation = tk.Label(
    root,
    textvariable=display_text,
    background="lightblue",
    height=2
)

def button_pressed(value):
    current = display_text.get()
    if current == "0":
        display_text.set(value)
    else:
        display_text.set(current + value)


operation.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)

index = 0

for row in range(1, 5):
    for col in range(5):
        operation_btn = tk.Button(
            root, 
            text=button_names[index],
            command=lambda text=button_names[index]: button_pressed(text)
        )
        operation_btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        index += 1

for col in range(5):
    root.grid_columnconfigure(col, weight=1)
for row in range(5):
    root.grid_rowconfigure(row, weight=1)
root.mainloop()
