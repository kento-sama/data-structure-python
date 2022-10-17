class Node:
    def __init__(self, value):
        self.value      = value
        self.left_node  = None
        self.right_node = None
        
class BinaryTree:
    def __init__(self, root = None):
        self.root = root
        
    # DFS
    def pre_order_traversal(self, node = None):
        if node is None:
            node = self.root
        if node:
            print(node.value)
            if node.left_node:
                self.pre_order_traversal(node.left_node)
            if node.right_node:
                self.pre_order_traversal(node.right_node)
                
    def in_order_traversal(self, node = None):
        if node is None:
            node = self.root
        if node:
            if node.left_node:
                self.in_order_traversal(node.left_node)
            
            print(node.value)
            
            if node.right_node:
                self.in_order_traversal(node.right_node)
                
    def post_order_traversal(self, node = None):
        if node is None:
            node = self.root
        if node:
            if node.left_node:
                self.post_order_traversal(node.left_node)
            if node.right_node:
                self.post_order_traversal(node.right_node)
            print(node.value)
            
    def delete(self, value):
        current_node = self.root
        if self.root:
            parent_deleted = None # None if the node to be deleted is a root
            while current_node and current_node.value != value:
                parent_deleted = current_node
                if current_node.value > value:
                    current_node = current_node.left_node
                else:
                    current_node = current_node.right_node
            
            if not current_node: # to be deleted value does not exist in the binary tree
                return False
            
            deleted_node = current_node # node to be deleted
            
            if current_node.right_node:
                parent = current_node
                current_node = current_node.right_node # current_node is the one to replace the node to be deleted
                while current_node.left_node:
                    parent = current_node
                    current_node = current_node.left_node

            elif current_node.left_node:
                parent = current_node
                current_node = current_node.left_node # current_node is the one to replace the node to be deleted
                while current_node.right_node:
                    parent = current_node
                    current_node = current_node.right_node
            else:
                # to be deleted node is a leaf
                if parent_deleted:
                    if parent_deleted.value < current_node.value:
                        parent_deleted.right_node = None
                    else:
                        parent_deleted.left_node = None
                else: # if there only the root
                    self.root = None
                return True
            
            if parent.left_node == current_node:
                parent.left_node = None
            elif parent.right_node == current_node:
                parent.right_node = None
            if current_node.right_node:
                if parent.value > current_node.right_node.value:
                    parent.left_node = current_node.right_node
                else:
                    parent.right_node = current_node.left_node
            
            deleted_node.value = current_node.value
            return True
    
    def insert(self, value):
        new_node = Node(value)
        current_node = self.root
        if self.root:
            while current_node:
                parent = current_node
                if current_node.value < new_node.value:
                    current_node = current_node.right_node
                else:
                    current_node = current_node.left_node
            if parent.value < new_node.value:
                parent.right_node = new_node
            else:
                parent.left_node = new_node
        else:
            self.root = new_node
            
    def search(self, value):
        current_node = self.root
        if self.root:
            while current_node:
                if current_node.value > value:
                    current_node = current_node.left_node
                elif current_node.value < value:
                    current_node = current_node.right_node
                else:
                    return True
        return False
            
new_tree = BinaryTree()
new_tree.insert(5)
new_tree.insert(2)
new_tree.insert(8)
new_tree.insert(1)
new_tree.insert(3)
new_tree.insert(7)
new_tree.insert(9)
new_tree.insert(0)
new_tree.insert(4)
new_tree.insert(6)
new_tree.insert(10)
new_tree.insert(8.5)
new_tree.insert(7.5)

print("----------------------")

new_tree.pre_order_traversal()

print("----------------------")

new_tree.in_order_traversal()

print("----------------------")

new_tree.post_order_traversal()
        
print("----------------------")
new_tree.delete(10)
new_tree.in_order_traversal()

print("----------------------")
print(new_tree.search(9))