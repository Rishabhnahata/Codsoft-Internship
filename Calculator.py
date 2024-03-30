# import tkinter as tk

# def button_click(symbol):
#     current = entry.get()
#     entry.delete(0, tk.END)
#     entry.insert(tk.END, current + symbol)

# def clear():
#     entry.delete(0, tk.END)

# def calculate():
#     try:
#         result = eval(entry.get())
#         entry.delete(0, tk.END)
#         entry.insert(tk.END, str(result))
#     except Exception as e:
#         entry.delete(0, tk.END)
#         entry.insert(tk.END, "Error")

# # Create the main window
# root = tk.Tk()
# root.title("Calculator")

# # Entry widget to display input and output
# entry = tk.Entry(root, width=35, borderwidth=5)
# entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# # Define buttons
# buttons = [
#     ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
#     ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
#     ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
#     ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
#     ('Clear', 5, 0), ('Close', 5, 1)
# ]

# # Create buttons
# for button_text, row, col in buttons:
#     button = tk.Button(root, text=button_text, padx=30, pady=20, command=lambda symbol=button_text: button_click(symbol))
#     button.grid(row=row, column=col)

# # Bind enter key to calculate function
# root.bind('<Return>', lambda event=None: calculate())

# # Run the main event loop
# root.mainloop()
import tkinter as tk

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operation_var.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            result = "Error: Cannot divide by zero"
        else:
            result = num1 / num2

    result_label.config(text="Result: " + str(result))

root = tk.Tk()
root.title("Simple Calculator")

# Entry fields
entry1 = tk.Entry(root)
entry1.grid(row=0, column=0, padx=5, pady=5)

entry2 = tk.Entry(root)
entry2.grid(row=0, column=1, padx=5, pady=5)

# Operation choice
operation_var = tk.StringVar(root)
operation_var.set("+")  # Default operation is addition
operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.grid(row=0, column=2, padx=5, pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
