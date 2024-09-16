import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = int(entry_length.get())
    
    # Define password characters
    characters = string.ascii_letters
    if var_special.get():
        characters += string.punctuation
    if var_numbers.get():
        characters += string.digits
    
    if length < 4:
        messagebox.showerror("Error", "Password length should be at least 4")
        return
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    entry_password.delete(0, tk.END)  # Clear previous password
    entry_password.insert(0, password)

# Creating the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.resizable(False, False)

# Length of password
label_length = tk.Label(root, text="Password Length:")
label_length.pack(pady=10)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# Include special characters
var_special = tk.IntVar()
check_special = tk.Checkbutton(root, text="Include Special Characters", variable=var_special)
check_special.pack(pady=5)

# Include numbers
var_numbers = tk.IntVar()
check_numbers = tk.Checkbutton(root, text="Include Numbers", variable=var_numbers)
check_numbers.pack(pady=5)

# Button to generate password
btn_generate = tk.Button(root, text="Generate Password", command=generate_password)
btn_generate.pack(pady=10)

# Display the generated password
entry_password = tk.Entry(root, font=("Arial", 14))
entry_password.pack(pady=5)

# Start the GUI loop
root.mainloop()
