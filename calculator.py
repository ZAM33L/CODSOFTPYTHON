import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

app = tk.Tk()
app.title("Calculator")

entry = tk.Entry(app, width=20, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4)

button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button_text in button_texts:
    tk.Button(
        app,
        text=button_text,
        padx=20,
        pady=20,
        font=('Arial', 20),
        command=lambda text=button_text: button_click(text) if text != '=' else calculate()
    ).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(app, text='C', padx=20, pady=20, font=('Arial', 20), command=clear).grid(row=5, column=0, columnspan=4)

app.mainloop()
