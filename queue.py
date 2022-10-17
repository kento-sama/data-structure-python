"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList():
    def __init__(self, element=None):
        self.head = element
        self.tail = element
        
    def insert_last(self, new_element):
        if self.tail:
            self.tail.next = new_element
            self.tail = self.tail.next
        else:
            self.head = new_element
            self.tail = new_element
    
    def delete_first(self):
        deleted = self.head
        if self.head == self.tail:
            self.tail = None
        if self.head:
            self.head = self.head.next
            deleted.next = None
            
        return deleted
    
    def see_first(self):
        return self.head
    
    def see_all(self):
        current = self.head
        if self.head:
            while current:
                current = current.next

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        deleted = self.storage[0]
        self.storage = self.storage[1:]
        return deleted
    
class QueueTwo:
    def __init__(self, element=None):
        self.ll = LinkedList(element)
        
    def enqueue(self, new_element):
        self.ll.insert_last(new_element)
    
    def peek(self):
        return self.ll.see_first()
    
    def dequeue(self):
        return self.ll.delete_first()
    
    def see_all(self):
        self.ll.see_all()
    
    
    
# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print(q.peek())

# Test dequeue
# Should be 1
print(q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print(q.dequeue())
# Should be 3
print(q.dequeue())
# Should be 4
print(q.dequeue())
q.enqueue(5)
# Should be 5
print(q.peek())

print("---------------")

el1 = Element(1)
el2 = Element(2)
el3 = Element(3)
el4 = Element(4)
el5 = Element(5)

q2 = QueueTwo()
q2.enqueue(el1)
q2.enqueue(el2)
q2.enqueue(el3)
q2.see_all()

# Test peek
# Should be 1
print(q2.peek().value)

# Test dequeue
# Should be 1
print(q2.dequeue().value)
q2.see_all()

# Test enqueue
q2.enqueue(el4)
q2.see_all()
# Should be 2
print(q2.dequeue().value)
# Should be 3
print(q2.dequeue().value)
# Should be 4
print(q2.dequeue().value)
q2.see_all()
q2.enqueue(el5)
q2.see_all()
# Should be 5
print(q2.peek().value)