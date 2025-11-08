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

    def insertBefore(self, nextNode, data):
        if nextNode is None:
            print("Next node cannot be NULL")
            return
        
        newNode = Node(data)
        newNode.prev = nextNode.prev
        nextNode.prev = newNode
        newNode.next = nextNode

        if newNode.prev is not None:
            newNode.prev.next = newNode
        else:
            self.head = newNode

if __name__ == "__main__":
    print("--- Activity 2 ---")
    
    trainList = LinkedList()
    trainList.add("Engine")
    trainList.add("Coach 1")
    trainList.add("Sleeper Coach")
    trainList.add("Pantry Car")
    
    print("Original train:")
    trainList.printList()

    s = trainList.head.next.next
    
    print("\nAdding 'VIP Coach' before 'Sleeper Coach'...")
    trainList.insertBefore(s, "VIP Coach")
    
    trainList.printList()