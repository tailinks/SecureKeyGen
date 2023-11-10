import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGeneratorApp:
    """
    A GUI application for generating random passwords.

    Attributes:
        root (tk.Tk): The main window of the application.
        length_var (tk.IntVar): Variable to store the desired password length.
        use_symbols_var (tk.BooleanVar): Variable to store the choice of including symbols.
        use_numbers_var (tk.BooleanVar): Variable to store the choice of including numbers.
        use_uppercase_var (tk.BooleanVar): Variable to store the choice of including uppercase letters.
        result_var (tk.StringVar): Variable to display the generated password.
    """
    def __init__(self, root: tk.Tk):
        """
        Initialize the application.

        Args:
            root (tk.Tk): The main window of the application.
        """
        self.root = root
        root.title('SecureKeyGen: Password Generator')

        # Create layout components
        ttk.Label(root, text='Password Length:').grid(row=0, column=0)
        self.length_var = tk.IntVar(value=12)  # Default length
        ttk.Entry(root, textvariable=self.length_var).grid(row=0, column=1)

        self.use_symbols_var = tk.BooleanVar()
        ttk.Checkbutton(root, text='Include Symbols', variable=self.use_symbols_var).grid(row=1, columnspan=2)

        self.use_numbers_var = tk.BooleanVar()
        ttk.Checkbutton(root, text='Include Numbers', variable=self.use_numbers_var).grid(row=2, columnspan=2)

        self.use_uppercase_var = tk.BooleanVar()
        ttk.Checkbutton(root, text='Include Uppercase Letters', variable=self.use_uppercase_var).grid(row=3, columnspan=2)

        ttk.Button(root, text='Generate Password', command=self.generate_password).grid(row=4, columnspan=2)

        self.result_var = tk.StringVar()
        ttk.Entry(root, textvariable=self.result_var, state='readonly').grid(row=5, columnspan=2)

    def generate_password(self) -> None:
        """
        Generate a random password based on user inputs and display it in the GUI.
        """
        length = self.length_var.get()
        use_symbols = self.use_symbols_var.get()
        use_numbers = self.use_numbers_var.get()
        use_uppercase = self.use_uppercase_var.get()

        # Define the character pool based on user choices
        characters = string.ascii_lowercase
        if use_symbols:
            characters += string.punctuation
        if use_numbers:
            characters += string.digits
        if use_uppercase:
            characters += string.ascii_uppercase

        # Generate the password
        password = ''.join(random.choice(characters) for _ in range(length))
        self.result_var.set(password)

if __name__ == '__main__':
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
