class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def isempty(self):
        return self.front is None

    def enqueue(self, data):
        newNode = Node(data)
        if self.isempty():
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        self.count += 1

    def dequeue(self):
        if self.isempty():
            print("Queue is empty!")
            return None
        pData = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.count -= 1
        return pData

    def peek(self):
        if self.isempty():
            print("Queue is empty!")
            return None
        return self.front.data

    def size(self):
        return self.count


queue = Queue()

print("Is the queue empty?:", queue.isempty())
print("Size of the queue:", queue.size())

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Size of the queue after enqueues:", queue.size())
print("Peek:", queue.peek())

dequeued_item = queue.dequeue()
print("Item dequeued:", dequeued_item)

print("Size of the queue after dequeue:", queue.size())
print("Peek after dequeue:", queue.peek())
