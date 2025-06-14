import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('todo.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    status TEXT DEFAULT 'Pending'
)
''')
conn.commit()

def load_tasks():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT id, title, status FROM tasks")
    for task in cursor.fetchall():
        listbox.insert(tk.END, f"{task[0]} - {task[1]} [{task[2]}]")

def add_task():
    title = entry.get()
    if title:
        cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        conn.commit()
        entry.delete(0, tk.END)
        load_tasks()
    else:
        messagebox.showwarning("Input Error", "Enter a task")

def mark_completed():
    try:
        task = listbox.get(listbox.curselection())
        task_id = int(task.split(" - ")[0])
        cursor.execute("UPDATE tasks SET status='Completed' WHERE id=?", (task_id,))
        conn.commit()
        load_tasks()
    except:
        messagebox.showwarning("Selection Error", "Select a task")

def delete_task():
    try:
        task = listbox.get(listbox.curselection())
        task_id = int(task.split(" - ")[0])
        cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        conn.commit()
        load_tasks()
    except:
        messagebox.showwarning("Selection Error", "Select a task")

app = tk.Tk()
app.title("To-Do List")

entry = tk.Entry(app, width=40)
entry.pack(pady=10)

add_button = tk.Button(app, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

listbox = tk.Listbox(app, width=50, height=10)
listbox.pack(pady=10)

complete_button = tk.Button(app, text="Mark Completed", width=20, command=mark_completed)
complete_button.pack(pady=5)

delete_button = tk.Button(app, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

load_tasks()
app.mainloop()
conn.close()
