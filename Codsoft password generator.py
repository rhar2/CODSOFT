import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    # Define character sets for password complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on desired complexity
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate password using random.choice()
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

# Create main application window
app = tk.Tk()
app.title("Password Generator")
app.configure(bg='#E8E8E8')

# Set custom font styles
font_bold = ('Helvetica', 12, 'bold')
font_normal = ('Helvetica', 12)

# Custom color scheme
bg_color = '#E8E8E8'
button_color = '#4CAF50'
button_hover_color = '#45a049'
button_fg_color = 'white'
entry_bg_color = 'white'
entry_fg_color = 'black'
text_bg_color = 'white'
text_fg_color = 'black'

# Round corners for widgets
app.option_add('*TCombobox*Listbox*background', entry_bg_color)
app.option_add('*TCombobox*Listbox*foreground', entry_fg_color)
app.option_add('*TCombobox*Listbox*selectBackground', button_hover_color)
app.option_add('*TCombobox*Listbox*selectForeground', button_fg_color)

# Create password length label and entry
length_label = tk.Label(app, text="Enter password length:", font=font_bold, bg=bg_color)
length_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
length_entry = tk.Entry(app, font=font_normal, bd=2, relief="solid", bg=entry_bg_color, fg=entry_fg_color)
length_entry.grid(row=0, column=1, padx=5, pady=5)

# Create generate button
generate_button = tk.Button(app, text="Generate Password", command=generate_and_display_password, font=font_bold, bg=button_color, fg=button_fg_color, activebackground=button_hover_color, bd=2, relief="raised")
generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='ew')

# Create password display text widget
password_display = tk.Text(app, width=30, height=5, font=font_normal, bd=2, relief="solid", bg=text_bg_color, fg=text_fg_color, state='disabled')
password_display.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='ew')

# Set weight for rows and columns to make them expandable
app.grid_rowconfigure(2, weight=1)
app.grid_columnconfigure(0, weight=1)

# Start the Tkinter event loop
app.mainloop()
