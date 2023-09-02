import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task!")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        pass

app = tk.Tk()
app.title("To-Do List App")

frame = tk.Frame(app)
frame.pack(pady=10)

listbox = tk.Listbox(
    frame,
    width=40,
    height=10,
    selectbackground="yellow"
)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(app, width=30)
entry.pack(pady=10)

add_button = tk.Button(app, text="Add Task", width=30, command=add_task)
add_button.pack()

delete_button = tk.Button(app, text="Delete Task", width=30, command=delete_task)
delete_button.pack()

app.mainloop()
