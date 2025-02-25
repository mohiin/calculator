

from tkinter import *
import math


def on_click(value):
    print("button is clicked")
    print(value)
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + value)

def evaluate():
    print("hello...")
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except Exception as e:
        print("except")
        entry.delete(0, END)
        entry.insert(END, "Error")

def scientific_function(val):
    print("scientific")
    print(val)
    try:
           value = float(entry.get())
           entry.delete(0, END)
           if val == "sin":
               entry.insert(END, str(math.sin(math.radians(value))))

           elif val == "cos":
               entry.insert(END, str(math.cos(math.radians(value))))
           elif val == "cos":
               entry.insert(END, str(math.cos(math.radians(value))))
           elif val == "tan":
               entry.insert(END, str(math.tan(math.radians(value))))
           elif val == "log":
               entry.insert(END, str(math.log10(value)))
           elif val == "ln":
               entry.insert(END, str(math.log(value)))
           elif val == "sqrt":
               entry.insert(END, str(math.sqrt(value)))
           elif val == "exp":
               entry.insert(END, str(math.exp(value)))
           elif val == "pow":
               entry.insert(END, str(math.pow(value, 2)))
           elif val == "e":
               entry.insert(END, str(math.exp(value)))
    except Exception as e:
           print(" e ")



def clear():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

root = Tk()
root.geometry("360x700")
root.title("Simple Calculator")
root.config(bg="#2e2e2e")

entry = Entry(root, font=("Arial", 20), borderwidth=0, relief="solid", justify="right", bg="#f0f0f0",)
entry.grid(row=0, column=0, columnspan=4)

# Button layout for digits and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Add number and operation buttons
for (text, row, col) in buttons:
    if text == "=":
        button = Button(root, text=text, font=('Arial', 20), height=1,relief="flat", bg="#4CAF50", fg="white", activebackground="#45a049", command=evaluate)
    else:
        button = Button(root, text=text, font=('Arial', 20), height=1, command=lambda t=text: on_click(t))
    button.grid(row=row, column=col, sticky="nsew")


#scienific buttons
scientific_buttons = [
    ("sin", "sin", 5, 0), ("cos", "cos", 5, 1), ("tan", "tan", 5,2),
    ("In", "In", 5,3), ("sqrt", "sqrt", 6, 0), ("exp","exp", 6, 1),
    ("x^2", "pow", 6, 2), ("e", "e", 6, 3)
]

for (text, function, row, col) in scientific_buttons:
    button = Button(root, text=text, command=lambda f=function: scientific_function(f))
    button.grid(row=row, column=col, sticky="nsew")

clear_button = Button(root, text="C", font=("Arial", 20), height=1, command=clear)
clear_button.grid(row=7, column=0, columnspan=2, sticky="nsew")

delete_button = Button(root, text="Del",  font=("Arial", 20), height=1, command=backspace)
delete_button.grid(row=7, column=2, columnspan=2, sticky="nsew")

# Configure the grid to make buttons expand evenly
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for i in range(7):
    root.grid_columnconfigure(i, weight=1)

# Add Hover Effect for Buttons (optional)
def on_enter(event):
    event.widget.config(bg="#45a049")

def on_leave(event):
    event.widget.config(bg="#4CAF50")



# Bind the hover effect to each button
# for (text, row, col) in buttons:
#     button = Button(root, text=text, font=('Arial', 20), height=2, relief="flat", bg="#4CAF50", fg="white", activebackground="#45a049", command=lambda t=text: on_click(t) if t != "=" else evaluate())
#     button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
#     button.bind("<Enter>", on_enter)
#     button.bind("<Leave>", on_leave)



root.mainloop()