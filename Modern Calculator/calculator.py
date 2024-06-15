from customtkinter import *

# Functions
def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    if number2 != 0:
        return number1 / number2
    else:
        return "Error: Division by zero"

# GUI
window = CTk()
window.title('Calculator')
window.geometry('300x400')
window.iconbitmap('calculator.ico')

# Entry fields for input
entry1 = CTkEntry(window)
entry1.pack(pady=10)

entry2 = CTkEntry(window)
entry2.pack(pady=10)

# Result display label
result_label = CTkLabel(window, text="Result:")
result_label.pack(pady=5)

result_var = StringVar()
result_label_value = CTkLabel(window, textvariable=result_var)
result_label_value.pack()

# Calculate based on selected transaction
def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == 'Add':
            result = addition(num1, num2)
        elif operation == 'Subtract':
            result = subtraction(num1, num2)
        elif operation == 'Multiply':
            result = multiplication(num1, num2)
        elif operation == 'Divide':
            result = division(num1, num2)
        else:
            result = "Error: Unknown operation"

        result_var.set(result)
    except ValueError:
        result_var.set("Error: Invalid input")

# Buttons for operations
button_add = CTkButton(window, text='Add', command=lambda: calculate('Add'))
button_add.pack(pady=5)

button_subtract = CTkButton(window, text='Subtract', command=lambda: calculate('Subtract'))
button_subtract.pack(pady=5)

button_multiply = CTkButton(window, text='Multiply', command=lambda: calculate('Multiply'))
button_multiply.pack(pady=5)

button_divide = CTkButton(window, text='Divide', command=lambda: calculate('Divide'))
button_divide.pack(pady=5)

window.mainloop()