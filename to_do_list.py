import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def mark_done():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(tk.END, f"✔️ {task}")
    except:
        messagebox.showwarning("Warning", "Please select a task to mark as done!")

# GUI setup
root = tk.Tk()
root.title("📝 To-Do List App")
root.geometry("400x500")
root.config(bg="#1e1e2e")

title_label = tk.Label(root, text="🧠 To-Do List", font=("Helvetica", 18, "bold"), bg="#1e1e2e", fg="white")
title_label.pack(pady=15)

frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, font=("Arial", 14), width=20)
task_entry.grid(row=0, column=0, padx=10)

add_button = tk.Button(frame, text="Add", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=add_task)
add_button.grid(row=0, column=1)

tasks_listbox = tk.Listbox(root, width=35, height=15, font=("Arial", 12), bg="#2e2e3e", fg="white", selectbackground="#4CAF50")
tasks_listbox.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

delete_button = tk.Button(btn_frame, text="Delete", font=("Arial", 12, "bold"), bg="#E74C3C", fg="white", command=delete_task)
delete_button.grid(row=0, column=0, padx=10)

done_button = tk.Button(btn_frame, text="Mark Done", font=("Arial", 12, "bold"), bg="#3498DB", fg="white", command=mark_done)
done_button.grid(row=0, column=1, padx=10)

root.mainloop()
