import tkinter as tk
import math

def button_click(symbol):
    current = entry.get()
    if current == "Error":
        entry.delete(0, tk.END)
        current = ""
    if symbol == "C":
        entry.delete(0, tk.END)
    elif symbol == "=":
        try:
            if "√" in current:
                number = float(current.split("√")[1])
                result = math.sqrt(number)
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(result))
            else:
                result = eval(current)
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif symbol == "√":
        entry.insert(tk.END, "√")
    else:
        entry.insert(tk.END, symbol)

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.configure(background="#444444")

# Create the entry widget
entry = tk.Entry(window, font=("Arial", 20), bg="#CCCCCC", fg="#333333")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Define the buttons layout and colors
buttons = [
    ('C', '(',')', '%', '/'),
    ('7', '8', '9', '*',''),
    ('4', '5', '6', '-',''),
    ('1', '2', '3', '+',''),
    ('√', '.', '0', '=','')
]

button_colors = {
    'bg': '#FFA500',
    'fg': '#000000'
}

# Create and place the buttons
for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        button = tk.Button(window, text=buttons[i][j], font=("Arial", 15), width=5, height=2,
                           command=lambda symbol=buttons[i][j]: button_click(symbol), **button_colors)
        button.grid(row=i+1, column=j, padx=5, pady=5, sticky="ew")

# Start the Tkinter event loop
window.mainloop()
