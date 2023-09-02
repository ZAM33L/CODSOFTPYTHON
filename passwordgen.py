import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    complexity = complexity_var.get()
    
    if complexity == 'Letters':
        characters = string.ascii_letters
    elif complexity == 'Letters + Digits':
        characters = string.ascii_letters + string.digits
    elif complexity == 'Letters + Digits + Special Characters':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return

    password =  ' '.join(random.choice(characters) for _ in range(length))
    password_display.config(text="Generated Password: " + password)

# Create the main window
app = tk.Tk()
app.title("Password Generator")

# Label for password length
length_label = tk.Label(app, text="Enter Password Length:")
length_label.pack()

# Entry field for password length
length_entry = tk.Entry(app)
length_entry.pack()

# Label for complexity level
complexity_label = tk.Label(app, text="Select Complexity Level:")
complexity_label.pack()

# Dropdown for complexity level
complexity_options = ['Letters', 'Letters + Digits', 'Letters + Digits + Special Characters']
complexity_var = tk.StringVar(app)
complexity_var.set(complexity_options[0])
complexity_dropdown = tk.OptionMenu(app, complexity_var, *complexity_options)
complexity_dropdown.pack()

# Button to generate password
generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack()

# Label to display generated password
password_display = tk.Label(app, text="")
password_display.pack()

# Run the main loop
app.mainloop()
