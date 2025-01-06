import tkinter as tk
from tkinter import messagebox

# Binary Tree Implementation
class TaskNode:
    def __init__(self, task):
        self.task = task
        self.left = None
        self.right = None

class TaskBinaryTree:
    def __init__(self):
        self.root = None

    def add_task(self, task):
        new_node = TaskNode(task)
        if not self.root:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, current, new_node):
        if new_node.task['priority'] < current.task['priority']:
            if current.left is None:
                current.left = new_node
            else:
                self._insert(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert(current.right, new_node)

    def get_tasks_in_priority_order(self):
        tasks = []
        self._in_order_traversal(self.root, tasks)
        return tasks

    def _in_order_traversal(self, node, tasks):
        if node:
            self._in_order_traversal(node.left, tasks)
            tasks.append(node.task)
            self._in_order_traversal(node.right, tasks)

    def find_task(self, priority):
        return self._search(self.root, priority)

    def _search(self, node, priority):
        if node is None:
            return None
        if node.task['priority'] == priority:
            return node.task
        elif priority < node.task['priority']:
            return self._search(node.left, priority)
        else:
            return self._search(node.right, priority)

# GUI Implementation
class CarMaintenanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Maintenance Service - Binary Tree")
        self.root.geometry("800x600")
        self.root.configure(bg="#f5f5f5")

        # Binary Tree
        self.task_tree = TaskBinaryTree()

        # GUI Components
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title = tk.Label(self.root, text="Car Maintenance Service", bg="#4CAF50", fg="white", font=("Arial", 24, "bold"))
        title.pack(pady=10)

        # Frames
        task_frame = tk.LabelFrame(self.root, text="Task Management", bg="#e3f2fd", font=("Arial", 12, "bold"))
        task_frame.place(x=20, y=70, width=350, height=500)

        display_frame = tk.LabelFrame(self.root, text="Display & Search", bg="#fbe9e7", font=("Arial", 12, "bold"))
        display_frame.place(x=400, y=70, width=370, height=500)

        # Task Management
        tk.Label(task_frame, text="Task Type:", bg="#e3f2fd", font=("Arial", 10)).place(x=10, y=20)
        self.task_type_entry = tk.Entry(task_frame, width=30)
        self.task_type_entry.place(x=100, y=20)

        tk.Label(task_frame, text="Priority:", bg="#e3f2fd", font=("Arial", 10)).place(x=10, y=60)
        self.priority_entry = tk.Entry(task_frame, width=30)
        self.priority_entry.place(x=100, y=60)

        tk.Label(task_frame, text="Customer Name:", bg="#e3f2fd", font=("Arial", 10)).place(x=10, y=100)
        self.customer_name_entry = tk.Entry(task_frame, width=30)
        self.customer_name_entry.place(x=100, y=100)

        tk.Button(task_frame, text="Add Task", bg="#64b5f6", fg="white", command=self.add_task).place(x=100, y=140)

        # Display and Search
        tk.Button(display_frame, text="Show Tasks in Priority Order", bg="#ffab91", fg="white", command=self.show_tasks).place(x=100, y=20)

        tk.Label(display_frame, text="Search Priority:", bg="#fbe9e7", font=("Arial", 10)).place(x=10, y=60)
        self.search_priority_entry = tk.Entry(display_frame, width=20)
        self.search_priority_entry.place(x=120, y=60)
        tk.Button(display_frame, text="Search Task", bg="#ff8a65", fg="white", command=self.search_task).place(x=250, y=60)

        self.display_area = tk.Text(display_frame, width=40, height=20)
        self.display_area.place(x=10, y=100)

    def add_task(self):
        task_type = self.task_type_entry.get()
        priority = self.priority_entry.get()
        customer_name = self.customer_name_entry.get()

        if task_type and priority.isdigit() and customer_name:
            task = {"type": task_type, "priority": int(priority), "customer": customer_name}
            self.task_tree.add_task(task)
            messagebox.showinfo("Success", "Task added successfully!")
            self.task_type_entry.delete(0, tk.END)
            self.priority_entry.delete(0, tk.END)
            self.customer_name_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill in all fields with valid data.")

    def show_tasks(self):
        tasks = self.task_tree.get_tasks_in_priority_order()
        self.display_area.delete(1.0, tk.END)
        if tasks:
            for task in tasks:
                self.display_area.insert(tk.END, f"Task: {task['type']}, Priority: {task['priority']}, Customer: {task['customer']}\n")
        else:
            self.display_area.insert(tk.END, "No tasks available.")

    def search_task(self):
        priority = self.search_priority_entry.get()
        if priority.isdigit():
            task = self.task_tree.find_task(int(priority))
            self.display_area.delete(1.0, tk.END)
            if task:
                self.display_area.insert(tk.END, f"Task: {task['type']}, Priority: {task['priority']}, Customer: {task['customer']}\n")
            else:
                self.display_area.insert(tk.END, f"No task found with priority {priority}.")
        else:
            messagebox.showerror("Error", "Please enter a valid priority.")

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = CarMaintenanceApp(root)
    root.mainloop()
