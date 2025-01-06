import tkinter as tk
from tkinter import messagebox
from collections import deque

class OrderDeque:
    def __init__(self, max_size):
        self.orders = deque(maxlen=max_size)
        self.max_size = max_size

    def add_order_front(self, order):
        self.orders.appendleft(order)

    def add_order_rear(self, order):
        self.orders.append(order)

    def remove_order_front(self):
        if self.orders:
            return self.orders.popleft()
        return None

    def remove_order_rear(self):
        if self.orders:
            return self.orders.pop()
        return None

    def display_orders(self):
        return list(self.orders)

class DequeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Order Management - Deque")
        self.root.geometry("800x600")
        self.root.configure(bg="#f5f5f5")

        # Order Deque
        self.deque = OrderDeque(max_size=5)

        # GUI Components
        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="Order Management - Deque", bg="#4CAF50", fg="white", font=("Arial", 20, "bold"))
        title.pack(pady=10)

        # Frames
        input_frame = tk.LabelFrame(self.root, text="Manage Orders", bg="#e3f2fd", font=("Arial", 12, "bold"))
        input_frame.place(x=20, y=70, width=350, height=500)

        display_frame = tk.LabelFrame(self.root, text="Order List", bg="#fbe9e7", font=("Arial", 12, "bold"))
        display_frame.place(x=400, y=70, width=370, height=500)

        # Input Frame
        tk.Label(input_frame, text="Order ID:", bg="#e3f2fd", font=("Arial", 10)).place(x=10, y=20)
        self.order_id_entry = tk.Entry(input_frame, width=25)
        self.order_id_entry.place(x=120, y=20)

        tk.Label(input_frame, text="Customer Name:", bg="#e3f2fd", font=("Arial", 10)).place(x=10, y=60)
        self.customer_name_entry = tk.Entry(input_frame, width=25)
        self.customer_name_entry.place(x=120, y=60)

        tk.Label(input_frame, text="Service:", bg="#e3f2fd", font=("Arial", 10)).place(x=10, y=100)
        self.service_entry = tk.Entry(input_frame, width=25)
        self.service_entry.place(x=120, y=100)

        tk.Button(input_frame, text="Add Front", bg="#64b5f6", fg="white", command=self.add_order_front).place(x=40, y=140)
        tk.Button(input_frame, text="Add Rear", bg="#64b5f6", fg="white", command=self.add_order_rear).place(x=150, y=140)
        tk.Button(input_frame, text="Remove Front", bg="#ff8a65", fg="white", command=self.remove_order_front).place(x=40, y=180)
        tk.Button(input_frame, text="Remove Rear", bg="#ff8a65", fg="white", command=self.remove_order_rear).place(x=150, y=180)

        # Display Frame
        self.display_area = tk.Text(display_frame, width=40, height=25)
        self.display_area.place(x=10, y=20)

        tk.Button(display_frame, text="Refresh Orders", bg="#ffab91", fg="white", command=self.refresh_orders).place(x=120, y=440)

    def add_order_front(self):
        order_id = self.order_id_entry.get()
        customer_name = self.customer_name_entry.get()
        service = self.service_entry.get()

        if order_id and customer_name and service:
            order = {"order_id": order_id, "customer": customer_name, "service": service}
            self.deque.add_order_front(order)
            messagebox.showinfo("Success", "Order added to the front!")
            self.clear_inputs()
            self.refresh_orders()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def add_order_rear(self):
        order_id = self.order_id_entry.get()
        customer_name = self.customer_name_entry.get()
        service = self.service_entry.get()

        if order_id and customer_name and service:
            order = {"order_id": order_id, "customer": customer_name, "service": service}
            self.deque.add_order_rear(order)
            messagebox.showinfo("Success", "Order added to the rear!")
            self.clear_inputs()
            self.refresh_orders()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def remove_order_front(self):
        removed_order = self.deque.remove_order_front()
        if removed_order:
            messagebox.showinfo("Success", f"Removed order from front: {removed_order}")
        else:
            messagebox.showerror("Error", "No orders to remove from front.")
        self.refresh_orders()

    def remove_order_rear(self):
        removed_order = self.deque.remove_order_rear()
        if removed_order:
            messagebox.showinfo("Success", f"Removed order from rear: {removed_order}")
        else:
            messagebox.showerror("Error", "No orders to remove from rear.")
        self.refresh_orders()

    def refresh_orders(self):
        orders = self.deque.display_orders()
        self.display_area.delete(1.0, tk.END)
        if orders:
            for idx, order in enumerate(orders):
                self.display_area.insert(tk.END, f"{idx + 1}. {order}\n")
        else:
            self.display_area.insert(tk.END, "No orders available.")

    def clear_inputs(self):
        self.order_id_entry.delete(0, tk.END)
        self.customer_name_entry.delete(0, tk.END)
        self.service_entry.delete(0, tk.END)

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = DequeApp(root)
    root.mainloop()
