from tkinter import Tk, Entry, Button, StringVar  # Import necessary classes and functions for GUI
import math  # Import math module for scientific calculations

# Define the Calculator class
class Calculator:
    def __init__(self, master):  # Constructor method, initializes the calculator UI
        # Configure main window (title, size, background color, and resize options)
        master.title("Scientific Calculator")  # Set window title
        master.geometry('380x590+10+10')  # Set window size (370x590 pixels) and position on screen (0,0)
        master.config(bg='lightblue')  # Set background color to light blue
        master.resizable(False, False)  # Disable resizing of the window

        # Initialize attributes for equation and input
        self.equation = StringVar()  # Variable to dynamically update input field
        self.entry_value = ''  # Initialize the input value as an empty string

        # Create input field
        Entry(
            width=20,  # Width of the input field
            bg='#fff',  # Background color (white)
            font=('Arial Bold', 28),  # Font style and size
            textvariable=self.equation  # Bind input field to equation variable
        ).place(x=0, y=0)  # Position the input field at (0, 0)

        # Create Standard Buttons (parentheses, clear, numbers, and basic operations)
        # Row 1: Parentheses, Modulus, Clear
        Button(width=11, height=4, text='(', bg='white', command=lambda: self.show('(')).place(x=10, y=50)
        Button(width=11, height=4, text=')', bg='white', command=lambda: self.show(')')).place(x=100, y=50)
        Button(width=11, height=4, text='%', bg='white', command=lambda: self.show('%')).place(x=190, y=50)
        Button(width=11, height=4, text='C', bg='white', command=self.clear).place(x=280, y=50)

        # Row 2: Numbers 7-9, Division
        Button(width=11, height=4, text='7', bg='white', command=lambda: self.show(7)).place(x=10, y=125)
        Button(width=11, height=4, text='8', bg='white', command=lambda: self.show(8)).place(x=100, y=125)
        Button(width=11, height=4, text='9', bg='white', command=lambda: self.show(9)).place(x=190, y=125)
        Button(width=11, height=4, text='/', bg='white', command=lambda: self.show('/')).place(x=280, y=125)

        # Row 3: Numbers 4-6, Multiplication
        Button(width=11, height=4, text='4', bg='white', command=lambda: self.show(4)).place(x=10, y=200)
        Button(width=11, height=4, text='5', bg='white', command=lambda: self.show(5)).place(x=100, y=200)
        Button(width=11, height=4, text='6', bg='white', command=lambda: self.show(6)).place(x=190, y=200)
        Button(width=11, height=4, text='*', bg='white', command=lambda: self.show('*')).place(x=280, y=200)

        # Row 4: Numbers 1-3, Subtraction
        Button(width=11, height=4, text='1', bg='white', command=lambda: self.show(1)).place(x=10, y=275)
        Button(width=11, height=4, text='2', bg='white', command=lambda: self.show(2)).place(x=100, y=275)
        Button(width=11, height=4, text='3', bg='white', command=lambda: self.show(3)).place(x=190, y=275)
        Button(width=11, height=4, text='-', bg='white', command=lambda: self.show('-')).place(x=280, y=275)

        # Row 5: Decimal, Zero, Equals, Addition
        Button(width=11, height=4, text='.', bg='white', command=lambda: self.show('.')).place(x=10, y=350)
        Button(width=11, height=4, text='0', bg='white', command=lambda: self.show(0)).place(x=100, y=350)
        Button(width=11, height=4, text='=', bg='white', command=self.solve).place(x=190, y=350)
        Button(width=11, height=4, text='+', bg='white', command=lambda: self.show('+')).place(x=280, y=350)

        # Scientific Buttons (for trigonometric and other advanced functions)
        # Row 6: sin, cos, tan, sqrt
        Button(width=11, height=4, text='sin', bg='white', command=lambda: self.scientific_func('sin')).place(x=10, y=425)
        Button(width=11, height=4, text='cos', bg='white', command=lambda: self.scientific_func('cos')).place(x=100, y=425)
        Button(width=11, height=4, text='tan', bg='white', command=lambda: self.scientific_func('tan')).place(x=190, y=425)
        Button(width=11, height=4, text='sqrt', bg='white', command=lambda: self.scientific_func('sqrt')).place(x=280, y=425)

        # Row 7: log, ln, π, e
        Button(width=11, height=4, text='log', bg='white', command=lambda: self.scientific_func('log')).place(x=10, y=500)
        Button(width=11, height=4, text='ln', bg='white', command=lambda: self.scientific_func('ln')).place(x=100, y=500)
        Button(width=11, height=4, text='π', bg='white', command=lambda: self.show(math.pi)).place(x=190, y=500)
        Button(width=11, height=4, text='e', bg='white', command=lambda: self.show(math.e)).place(x=280, y=500)

    # Append a value to the current input
    def show(self, value):
        self.entry_value += str(value)  # Add value to the current input
        self.equation.set(self.entry_value)  # Update the input field

    # Clear the input field
    def clear(self):
        self.entry_value = ''  # Reset the input string
        self.equation.set(self.entry_value)  # Clear the input field

    # Evaluate the current equation
    def solve(self):
        try:
            result = eval(self.entry_value)  # Evaluate the equation
            self.equation.set(result)  # Display the result
        except Exception as e:
            self.equation.set("Error")  # Display "Error" if evaluation fails

    # Perform scientific calculations
    def scientific_func(self, func_name):
        try:
            value = eval(self.entry_value)  # Get the input value
            # Perform the required function
            if func_name == 'sin':
                result = math.sin(math.radians(value))  # Sine of the input
            elif func_name == 'cos':
                result = math.cos(math.radians(value))  # Cosine of the input
            elif func_name == 'tan':
                result = math.tan(math.radians(value))  # Tangent of the input
            elif func_name == 'sqrt':
                result = math.sqrt(value)  # Square root
            elif func_name == 'log':
                result = math.log10(value)  # Logarithm base 10
            elif func_name == 'ln':
                result = math.log(value)  # Natural logarithm
            self.equation.set(result)  # Display the result
            self.entry_value = str(result)  # Update the input with the result
        except Exception as e:
            self.equation.set("Error")  # Display "Error" if calculation fails

# Main program execution
root = Tk()  # Create the main application window
Calculator(root)  # Instantiate the Calculator class with the root window
root.mainloop()  # Start the event loop (keeps the application running)
