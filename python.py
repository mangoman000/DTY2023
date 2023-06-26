#importing the libary tkinter 
import tkinter as tk

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)

#Function for zero button
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

#Function for clear button
def button_clear():
    entry.delete(0, tk.END)

#Function for equals button
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

#Buttons one to nine
for i in range(9):
    button = tk.Button(root, text=str(i + 1), padx=20, pady=10, command=lambda i=i: button_click(i + 1))
    button.grid(row=(i // 3) + 1, column=i % 3)

#Buttons for special characters, plus, minus, multiply and divide
operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    button = tk.Button(root, text=operator, padx=20, pady=10, command=lambda operator=operator: button_click(operator))
    button.grid(row=i + 1, column=3)

button_zero = tk.Button(root, text='0', padx=20, pady=10, command=lambda: button_click(0))
button_zero.grid(row=4, column=1)

button_clear = tk.Button(root, text='C', padx=20, pady=10, command=button_clear)
button_clear.grid(row=4, column=0)

button_equal = tk.Button(root, text='=', padx=20, pady=10, command=button_equal)
button_equal.grid(row=4, column=2)

root.mainloop()
