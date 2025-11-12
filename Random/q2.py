class Node:
    def __init(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Dll:
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
        newNode.prev=current

    

    def displayReverse(self):
        current=self.head
        if not current:
            print("None")
            return
        while current.next:
            current=current.next
        
        while current:
            print(current.data,end="<->")
            current=current.prev
        print('None')

        def search(self, key, data):
            newNode = Node(data)
            current = self.head
            while current:
                if current.data == key:
                    # link newNode after current
                    newNode.next = current.next
                    newNode.prev = current
                    if current.next:
                        current.next.prev = newNode
                    current.next = newNode
                    return True
                current = current.next
            return False 

        def delete(self, key):
            current = self.head
            while current:
                if current.data == key:
                    # unlink current
                    if current.prev:
                        current.prev.next = current.next
                    else:
                        # deleting head
                        self.head = current.next
                    if current.next:
                        current.next.prev = current.prev
                    return True
                current = current.next
            return False
        def display(self):
            current=self.head
            while current:
                print(current.data,end="<->")
                current=current.next
            print("None")


                    
dll=Dll()
dll.append(10)
dll.append(20)
dll.append(30)
dll.display()          # Output: 10<->20<->30<->None
dll.displayReverse()   # Output: 30<->20<->10<->None
print(dll.search(20,30))  # Output: True