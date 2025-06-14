import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result.set(num1 + num2)
        elif operation == '-':
            result.set(num1 - num2)
        elif operation == '*':
            result.set(num1 * num2)
        elif operation == '/':
            if num2 != 0:
                result.set(num1 / num2)
            else:
                result.set("Error: Div by 0")
    except ValueError:
        result.set("Invalid Input")


root = tk.Tk()
root.title("Simple Calculator")
root.geometry('500x300')


entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

tk.Label(root, text="Number 1:").grid(row=0, column=0)
tk.Label(root, text="Number 2:").grid(row=1, column=0)


operation_var = tk.StringVar(value='+')

tk.Button(root, text="+", command=lambda: operation_var.set('+')).grid(row=2, column=0)
tk.Button(root, text="-", command=lambda: operation_var.set('-')).grid(row=2, column=1)
tk.Button(root, text="*", command=lambda: operation_var.set('*')).grid(row=2, column=2)
tk.Button(root, text="/", command=lambda: operation_var.set('/')).grid(row=2, column=3)


tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=1)


result = tk.StringVar()
tk.Label(root, text="Result:").grid(row=4, column=0)
tk.Label(root, textvariable=result).grid(row=4, column=1)

root.mainloop()
