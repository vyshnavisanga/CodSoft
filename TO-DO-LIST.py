import tkinter as tk
class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do-List")
        self.tasks = []
        self.task_list = tk.Listbox(self.root, width= 60,height=15)
        self.task_list.pack(fill="both", expand=True)
        self.entry_field = tk.Entry(self.root, width=40)
        self.entry_field.pack(fill="x")
        self.add_button = tk.Button(self.root, text="Add", command=self.add_task, bg="blue", fg="white")
        self.add_button.pack(fill="x")
        self.update_button = tk.Button(self.root, text="Update", command=self.update_task, bg="yellow")
        self.update_button.pack(fill="x")
        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_task, bg="green", fg="white")
        self.delete_button.pack(fill="x")
    def add_task(self):
        task = self.entry_field.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert("end", task)
            self.entry_field.delete(0, "end")
    def update_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            task = self.entry_field.get()
            if task:
                self.tasks[task_index] = task
                self.task_list.delete(task_index)
                self.task_list.insert(task_index, task)
                self.entry_field.delete(0, "end")
        except:
            print("Select a task to update")
    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.tasks.pop(task_index)
            self.task_list.delete(task_index)
        except:
            print("Select a task to delete")
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoList(root)
    root.mainloop()