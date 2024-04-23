import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
        password = generate_password(length)
        password_display.config(state='normal')
        password_display.delete(1.0, tk.END)
        password_display.insert(tk.END, password)
        password_display.config(state='disabled')
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer for the password length.")


app = tk.Tk()
app.title("Password Generator")
app.configure(bg='#F0F0F0')

length_label = tk.Label(app, text="Enter password length:", bg='#F0F0F0')
length_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
length_entry = tk.Entry(app)
length_entry.grid(row=0, column=1, padx=5, pady=5)


generate_button = tk.Button(app, text="Generate Password", command=generate_and_display_password, bg='#4CAF50', fg='white')
generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)


password_display = tk.Text(app, width=30, height=5, state='disabled')
password_display.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
app.mainloop()
