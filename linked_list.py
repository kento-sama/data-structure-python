from locale import currency


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head: # check if head is not empty
            while current.next: # while next is not empty
                current = current.next # traverse to next link until it's empty
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        i = 1
        current = self.head
        if self.head:
            while i < position:
                if current is not None:
                    current = current.next
                i += 1
            return current
        return None
    
    def insert(self, new_element, position):
        i = 1
        current = self.head
        if self.head:
            while i < position - 1:
                current = current.next
                i += 1
            if current.next is not None:
                new_element.next = current.next   
            current.next = new_element
    
    
    def delete(self, value):
        current = self.head
        prev = None
        if self.head:
            while current.value != value and current is not None:
                prev = current
                current = current.next
            if prev is None:
                self.head = current.next
            else:
                prev.next = current.next
            
            
            

# Test cases
# Set up some Elements
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print(ll.get_position(3).value)
#
# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)
        