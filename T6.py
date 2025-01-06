import tkinter as tk
from tkinter import messagebox

# Singly Linked List Node
class Node:
    def __init__(self, order_id, customer_name, service_type):
        self.order_id = order_id
        self.customer_name = customer_name
        self.service_type = service_type
        self.next = None

# Singly Linked List for managing orders
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_order(self, order_id, customer_name, service_type):
        new_node = Node(order_id, customer_name, service_type)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_order(self, order_id):
        current = self.head
        previous = None
        while current:
            if current.order_id == order_id:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False

    def display_orders(self):
        orders = []
        current = self.head
        while current:
            orders.append(f"Order ID: {current.order_id}, Customer: {current.customer_name}, Service: {current.service_type}")
            current = current.next
        return orders

# Tkinter GUI for Singly Linked List
class CarMaintenanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Maintenance Orders - Singly Linked List")
        self.root.geometry("600x400")
        self.root.configure(bg="#f5f5f5")

        # Linked List to track orders
        self.orders_list = SinglyLinkedList()

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="Car Maintenance Service Orders", bg="#4CAF50", fg="white", font=("Arial", 20, "bold"))
        title.pack(pady=10)

        # Input Form
        input_frame = tk.LabelFrame(self.root, text="Order Details", bg="#e3f2fd", font=("Arial", 12, "bold"))
        input_frame.place(x=20, y=70, width=350, height=250)

        tk.Label(input_frame, text="Order ID:", bg="#e3f2fd", font=("Arial", 10)).place(x=10, y=20)
        self.order_id_entry = tk.Entry(input_frame, width=25)
        self.order_id_entry.place(x=120, y=20)

        tk.Label(input_frame, text="Customer Name:", bg="#e3f2fd", font=("Arial", 10)).place(x=10, y=60)
        self.customer_name_entry = tk.Entry(input_frame, width=25)
        self.customer_name_entry.place(x=120, y=60)

        tk.Label(input_frame, text="Service Type:", bg="#e3f2fd", font=("Arial", 10)).place(x=10, y=100)
        self.service_type_entry = tk.Entry(input_frame, width=25)
        self.service_type_entry.place(x=120, y=100)

        tk.Button(input_frame, text="Add Order", bg="#64b5f6", fg="white", command=self.add_order).place(x=40, y=140)
        tk.Button(input_frame, text="Remove Order", bg="#ff8a65", fg="white", command=self.remove_order).place(x=150, y=140)

        # Display Frame
        display_frame = tk.LabelFrame(self.root, text="Current Orders", bg="#fbe9e7", font=("Arial", 12, "bold"))
        display_frame.place(x=400, y=70, width=170, height=250)

        self.display_area = tk.Text(display_frame, width=30, height=10)
        self.display_area.place(x=10, y=20)

        tk.Button(display_frame, text="Refresh Orders", bg="#ffab91", fg="white", command=self.refresh_orders).place(x=50, y=200)

    def add_order(self):
        order_id = self.order_id_entry.get()
        customer_name = self.customer_name_entry.get()
        service_type = self.service_type_entry.get()

        if order_id and customer_name and service_type:
            self.orders_list.add_order(order_id, customer_name, service_type)
            messagebox.showinfo("Success", "Order added successfully!")
            self.clear_inputs()
            self.refresh_orders()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def remove_order(self):
        order_id = self.order_id_entry.get()

        if order_id:
            success = self.orders_list.remove_order(order_id)
            if success:
                messagebox.showinfo("Success", f"Order {order_id} removed successfully!")
            else:
                messagebox.showerror("Error", f"Order {order_id} not found.")
            self.refresh_orders()
        else:
            messagebox.showerror("Error", "Please enter the Order ID to remove.")

    def refresh_orders(self):
        orders = self.orders_list.display_orders()
        self.display_area.delete(1.0, tk.END)
        if orders:
            for order in orders:
                self.display_area.insert(tk.END, f"{order}\n")
        else:
            self.display_area.insert(tk.END, "No orders available.")

    def clear_inputs(self):
        self.order_id_entry.delete(0, tk.END)
        self.customer_name_entry.delete(0, tk.END)
        self.service_type_entry.delete(0, tk.END)

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = CarMaintenanceApp(root)
    root.mainloop()
