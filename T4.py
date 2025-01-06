import tkinter as tk
from tkinter import ttk

class TreeNode:
    def __init__(self, name):
        """
        Initializes a tree node.
        :param name: Name of the node (e.g., category or service name).
        """
        self.name = name
        self.children = []

    def add_child(self, child_node):
        """
        Adds a child node to this node.
        :param child_node: TreeNode to be added as a child.
        """
        self.children.append(child_node)

    def display_tree(self, level=0):
        """
        Recursively prints the tree structure.
        :param level: Current depth of the tree for formatting.
        """
        print(" " * level * 4 + f"- {self.name}")
        for child in self.children:
            child.display_tree(level + 1)


# Example Hierarchical Tree
def create_service_tree():
    """
    Creates a sample tree structure for the subscription-based car maintenance service.
    """
    # Root
    root = TreeNode("Car Maintenance Services")

    # Level 1
    oil_services = TreeNode("Oil Services")
    tire_services = TreeNode("Tire Services")
    engine_services = TreeNode("Engine Services")

    # Add Level 1 to root
    root.add_child(oil_services)
    root.add_child(tire_services)
    root.add_child(engine_services)

    # Level 2 for Oil Services
    oil_change = TreeNode("Oil Change")
    oil_filter_replacement = TreeNode("Oil Filter Replacement")
    oil_services.add_child(oil_change)
    oil_services.add_child(oil_filter_replacement)

    # Level 2 for Tire Services
    tire_rotation = TreeNode("Tire Rotation")
    tire_replacement = TreeNode("Tire Replacement")
    tire_services.add_child(tire_rotation)
    tire_services.add_child(tire_replacement)

    # Level 2 for Engine Services
    engine_diagnosis = TreeNode("Engine Diagnosis")
    spark_plug_replacement = TreeNode("Spark Plug Replacement")
    engine_services.add_child(engine_diagnosis)
    engine_services.add_child(spark_plug_replacement)

    return root


class TreeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Service Hierarchy - Tree View")
        self.root.geometry("600x400")
        self.root.configure(bg="#f5f5f5")

        # TreeView Widget
        self.tree = ttk.Treeview(root)
        self.tree.heading("#0", text="Car Maintenance Service Hierarchy", anchor="w")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Populate Tree
        self.populate_tree()

    def populate_tree(self):
        service_tree = create_service_tree()
        self.add_node_to_tree(service_tree)

    def add_node_to_tree(self, node, parent=""):
        """
        Recursively adds nodes to the TreeView widget.
        :param node: Current TreeNode object to be added.
        :param parent: Parent ID in the TreeView widget.
        """
        tree_id = self.tree.insert(parent, "end", text=node.name)
        for child in node.children:
            self.add_node_to_tree(child, parent=tree_id)


if __name__ == "__main__":
    root = tk.Tk()
    app = TreeApp(root)
    root.mainloop()
