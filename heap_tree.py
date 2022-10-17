# child is (index + 1) * 2 and ((index + 1) * 2) + 1

class HeapTree:
    def __init__(self):
        self.tree = []
    
    def search(self, find_val):
        for i in self.tree:
            if self.tree[i] == find_val:
                return i
        return -1
    
    def insert(self, new_val):
        if self.tree:
            self.tree.append(new_val)
            current_index = len(self.tree) - 1
            self.heapify(current_index)
            # parent_index = (len(self.tree) // 2) - 1
            # while self.tree[current_index] > self.tree[parent_index] and parent_index >= 0:
            #     self.tree[current_index], self.tree[parent_index] = self.tree[parent_index], self.tree[current_index]
            #     current_index = parent_index
            #     parent_index = ((current_index + 1) // 2) - 1
        else:
            self.tree.append(new_val)
            
    def heapify(self, current_index=0):
        l = (current_index * 2) + 1
        r = l + 1
        if l >= len(self.tree):
            parent_index = ((current_index + 1) // 2) - 1
            while self.tree[current_index] > self.tree[parent_index] and parent_index >= 0:
                self.tree[current_index], self.tree[parent_index] = self.tree[parent_index], self.tree[current_index]
                current_index = parent_index
                parent_index = ((current_index + 1) // 2) - 1
        else:
            self.heapify(l)
        
        if  r >= len(self.tree):
            parent_index = ((current_index + 1) // 2) - 1
            while self.tree[current_index] > self.tree[parent_index] and parent_index >= 0:
                self.tree[current_index], self.tree[parent_index] = self.tree[parent_index], self.tree[current_index]
                current_index = parent_index
                parent_index = ((current_index + 1) // 2) - 1
        else:
            self.heapify(r)
            
    def breath_first_traversal(self):
        for i in self.tree:
            print(i)
            
    #dfs traversals
    def pre_order_traversal(self, current_index=0):
        if self.tree:
            if current_index >= len(self.tree):
                return
            print(self.tree[current_index])
            left_child = (current_index * 2) + 1
            right_child = left_child + 1
            self.pre_order_traversal(left_child)
            self.pre_order_traversal(right_child)
            
    def in_order_traversal(self, current_index=0):
        if self.tree:
            if current_index >= len(self.tree):
                return
            left_child = (current_index * 2) + 1
            right_child = left_child + 1
            self.in_order_traversal(left_child)
            print(self.tree[current_index])
            self.in_order_traversal(right_child)
            
    def post_order_traversal(self, current_index=0):
        if self.tree:
            if current_index >= len(self.tree):
                return
            left_child = (current_index * 2) + 1
            right_child = left_child + 1
            self.post_order_traversal(left_child)
            self.post_order_traversal(right_child)
            print(self.tree[current_index])
    
    def delete(self, del_val):
        deleted_index = None
        for i in range(len(self.tree)):
            if self.tree[i] == del_val:
                deleted_index = i
                break
        if deleted_index is not None:
            self.tree[deleted_index] = self.tree.pop()
            self.heapify(deleted_index)
            
    
new_heap = HeapTree()
new_heap.insert(5)
print(new_heap.tree)
new_heap.insert(8)
print(new_heap.tree)
new_heap.insert(9)
print(new_heap.tree)
new_heap.insert(7)
print(new_heap.tree)
new_heap.insert(4)
print(new_heap.tree)
new_heap.insert(11)
print(new_heap.tree)
new_heap.insert(3)
print(new_heap.tree)
new_heap.pre_order_traversal()
print("------------------")
new_heap.in_order_traversal()
print("------------------")
new_heap.post_order_traversal()
print("------------------")
new_heap.breath_first_traversal()
print("------------------")
new_heap1 = HeapTree()
new_heap1.insert(3)
new_heap1.insert(4)
new_heap1.insert(5)
new_heap1.insert(7)
new_heap1.insert(8)
new_heap1.insert(9)
new_heap1.insert(11)

print(new_heap1.tree)
new_heap1.delete(11)
print(new_heap1.tree)