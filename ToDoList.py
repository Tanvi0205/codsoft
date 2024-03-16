import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog as simpledialog

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.master.configure(bg = "Antique White") 
         
        self.tasks = []
        
        self.task_var = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
     
        tk.Label(self.master, text="        Enter the Task:").grid(row=0, column=0, sticky="w")
        self.task_entry = tk.Entry(self.master, textvariable=self.task_var)
        self.task_entry.grid(row=0, column=1, padx=5, pady=5)
        
       
        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=2, column=0, padx=5, pady=5)
        
       
        self.task_listbox = tk.Listbox(self.master, width=50, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=5, padx=5, pady=5)
        
        
        self.delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=2, padx=5, pady=5)
       
        self.update_button = tk.Button(self.master, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=1, padx=5, pady=5)
        
       
        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.quit)
        self.exit_button.grid(row=2, column=4, padx=5, pady=5)
    
    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    
    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.task_listbox.get(index)
            self.task_listbox.delete(index)
            self.tasks.remove(task)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")
    
    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.task_listbox.get(index)
            updated_task = simpledialog.askstring("Update Task", f"Update task '{task}' to:")
            if updated_task:
                self.tasks[index] = updated_task
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, updated_task)
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
