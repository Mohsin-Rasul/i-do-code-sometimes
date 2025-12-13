class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        newNode=Node(data)
        if not self.head:
            self.head=newNode
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=newNode

    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")

    def delete(self, key):
        # handle empty list
        if not self.head:
            return False
        # handle deleting head
        temp=self.head
        if temp.data == key:
            self.head = temp.next
            return True
        # walk and check the next node (no prev variable needed)
        current = self.head
        while current.next:
            t=current.next
            if t.data == key:
                current.next = t.next
                return True
            current = current.next
        return False
    
    def search(self,key):
        current=self.head
        while current:
            if current.data==key:
                return True
            current=current.next
        return False
l=LinkedList()
l.append(10)
l.append(30)
l.append(71)
l.display()
print(l.search(30))  # Output: True
print(l.search(50))  # Output: False
        
