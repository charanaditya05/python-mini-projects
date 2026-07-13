import tkinter as tk

tasks=[]

def add_task():
    task=task_entry.get()
    tasks.append({
        "task": task,
        "completed": False
        })
    task_entry.delete(0,tk.END)
    refresh_listbox()
    
def refresh_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        if task["completed"]:
            display_text = "☑ " + task["task"]
        else:
            display_text = "☐ " + task["task"]
        task_listbox.insert(tk.END, display_text)





window=tk.Tk()
window.title("To Do List")
window.geometry("500x600")
window.resizable(False, False)

task_label=tk.Label(window,text="Task")
task_label.pack()

task_entry = tk.Entry(window)
task_entry.pack()

AddBtn=tk.Button(window,text="Add Task",command=add_task)
AddBtn.pack()

task_listbox=tk.Listbox(window,height=10)
task_listbox.pack()

window.mainloop()