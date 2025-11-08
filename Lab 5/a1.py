class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        newNode = Node(data)
        temp = self.head
        newNode.next = None
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            return
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp

    def printList(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        
        print("NULL <-> ", end="")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("NULL")

    
    def insertAfter(self, prevNode, data):
        if prevNode is None:
            print("Previous node cannot be NULL")
            return

        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode
        newNode.prev = prevNode
        if newNode.next is not None:
            newNode.next.prev = newNode

if __name__ == "__main__":
    print("--- Activity 1 ---")
    
    myList = LinkedList()
    
    myList.add(10)
    myList.add(20)
    myList.add(40)
    
    print("Original list:")
    myList.printList()

    node20 = myList.head.next
    
    print("\nInserting 30 after 20...")
    myList.insertAfter(node20, 30)
    myList.printList()