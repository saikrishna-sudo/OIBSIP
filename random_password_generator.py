import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import string
import pyperclip

# Function to generate password
def generate_password():
    length = length_var.get()
    include_uppercase = uppercase_var.get()
    include_numbers = numbers_var.get()
    include_special = special_var.get()

    if length < 4:
        messagebox.showwarning("Password Length", "Password length should be at least 4.")
        return

    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")
    else:
        messagebox.showwarning("Copy Error", "No password to copy.")

# Setting up the main application window
root = tk.Tk()
root.title("Advanced Password Generator")

# Password length
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
length_var = tk.IntVar(value=12)
length_spinbox = tk.Spinbox(root, from_=4, to_=32, textvariable=length_var)
length_spinbox.grid(row=0, column=1, padx=10, pady=5, sticky="w")

# Include uppercase letters
uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Include numbers
numbers_var = tk.BooleanVar()
numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=numbers_var)
numbers_check.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Include special characters
special_var = tk.BooleanVar()
special_check = tk.Checkbutton(root, text="Include Special Characters", variable=special_var)
special_check.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Generated password entry
password_entry = tk.Entry(root, width=25, font=("Helvetica", 12))
password_entry.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Generate password button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Copy to clipboard button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
