# Import necessary modules from the tkinter library
from tkinter import Tk, Entry, Button, StringVar

# Define the Calculator class
class Calculator:
    def __init__(self, master):
        master.title("Calculator") # Set the title of the calculator window
        master.geometry('357x420+0+0') # Set the size and position of the calculator window
        master.config(bg='lightblue') # Set the background color of the calculator window
        master.resizable(False, False) # Prevent resizing the calculator window
        self.equation = StringVar() # Create a StringVar to hold the equation input
        self.entry_value = '' # Variable to store the input value

        # Create an entry field for displaying the equation
        Entry(width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        # Create calculator buttons with their respective commands and positions
        Button(width=11, height=4, text='(', relief='flat', bg='white', command=lambda: self.show('(')).place(x=0, y=50)
        Button(width=11, height=4, text=')', relief='flat', bg='white', command=lambda: self.show(')')).place(x=90, y=50)
        Button(width=11, height=4, text='%', relief='flat', bg='white', command=lambda: self.show('%')).place(x=180, y=50)
        Button(width=11, height=4, text='1', relief='flat', bg='white', command=lambda: self.show(1)).place(x=0, y=125)
        Button(width=11, height=4, text='2', relief='flat', bg='white', command=lambda: self.show(2)).place(x=90, y=125)
        Button(width=11, height=4, text='3', relief='flat', bg='white', command=lambda: self.show(3)).place(x=180, y=125)
        Button(width=11, height=4, text='4', relief='flat', bg='white', command=lambda: self.show(4)).place(x=0, y=200)
        Button(width=11, height=4, text='5', relief='flat', bg='white', command=lambda: self.show(5)).place(x=90, y=200)
        Button(width=11, height=4, text='6', relief='flat', bg='white', command=lambda: self.show(6)).place(x=180, y=200)
        Button(width=11, height=4, text='7', relief='flat', bg='white', command=lambda: self.show(7)).place(x=0, y=275)
        Button(width=11, height=4, text='8', relief='flat', bg='white', command=lambda: self.show(8)).place(x=180, y=275)
        Button(width=11, height=4, text='9', relief='flat', bg='white', command=lambda: self.show(9)).place(x=90, y=275)
        Button(width=11, height=4, text='0', relief='flat', bg='white', command=lambda: self.show(0)).place(x=90, y=350)
        Button(width=11, height=4, text='.', relief='flat', bg='white', command=lambda: self.show('.')).place(x=180, y=350)
        Button(width=11, height=4, text='+', relief='flat', bg='white', command=lambda: self.show('+')).place(x=270, y=275)
        Button(width=11, height=4, text='-', relief='flat', bg='white', command=lambda: self.show('-')).place(x=270, y=200)
        Button(width=11, height=4, text='/', relief='flat', bg='white', command=lambda: self.show('/')).place(x=270, y=50)
        Button(width=11, height=4, text='x', relief='flat', bg='white', command=lambda: self.show('*')).place(x=270, y=125)
        Button(width=11, height=4, text='=', relief='flat', command=self.solve).place(x=270, y=350)
        Button(width=11, height=4, text='C', relief='flat', command=self.clear).place(x=0, y=350)

    # Method to display the pressed button's value on the entry field
    def show(self, value):
        self.entry_value += str(value) # Append the button's value to the current equation
        self.equation.set(self.entry_value) # Update the entry field to reflect the equation

    # Method to clear the entry field
    def clear(self):
        self.entry_value = '' # Reset the entry value and clear the equation
        self.equation.set(self.entry_value)

    # Method to evaluate the equation
    def solve(self):
        try:
            # Evaluate the equation entered and set the result in the entry field
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception as e:
            # Handle errors by showing "Error" in the entry field
            self.equation.set("Error")

# Main program execution
root = Tk()  # Create the main application window
Calculator(root)  # Instantiate the Calculator class with the root window
root.mainloop()  # Start the event loop (keeps the application running)