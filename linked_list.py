class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Always maintain this for O(1) insertion

    def has_cycle(self)->bool:
        if self.head == None or self.head.next == None:
            return False
        fast = slow = self.head
       
        while(fast.next!=None and slow.next != None):
            if fast.next.next!=None:
                fast = fast.next.next
            else: return False
            slow = slow.next
            if fast == slow:
                return True
        return False



    def insert_at_beg(self, data):
        temp = Node(data)
        if not self.head:
            self.head = self.tail = temp
        else:
            temp.next = self.head
            self.head = temp

    def insert_at_end(self, data):
        """Optimized to O(1) using the tail pointer"""
        temp = Node(data)
        if not self.head:
            self.head = self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp

    def delete_at_beg(self):
        if not self.head:
            return None
        
        data = self.head.data
        self.head = self.head.next
        
        # If list becomes empty, update tail
        if not self.head:
            self.tail = None
        return data

    def delete_at_end(self):
        """O(n) complexity because we must find the second-to-last node"""
        if not self.head:
            return None
        
        # Case: Only one element
        if self.head == self.tail:
            data = self.head.data
            self.head = self.tail = None
            return data

        # Case: Multiple elements
        current = self.head
        while current.next != self.tail:
            current = current.next
        
        data = self.tail.data
        current.next = None
        self.tail = current
        return data

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty List")
            
sll = SinglyLinkedList()





a = sll.has_cycle()
print(a)



