class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insertnode(self.root, data)

    def insertnode(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insertnode(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insertnode(node.right, data)

    def delete(self, data):
        self.root = self.deletenode(self.root, data)

    def deletenode(self, node, data):
        if node is None:
            return node
        
        if data < node.data:
            node.left = self.deletenode(node.left, data)
        elif data > node.data:
            node.right = self.deletenode(node.right, data)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            
            temp = self.getmin(node.right)
            node.data = temp.data
            node.right = self.deletenode(node.right, temp.data)
        return node

    def getmin(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')

    def isbalanced(self, node):
        if node is None:
            return True
            
        leftheight = self.getheight(node.left)
        rightheight = self.getheight(node.right)
        
        diff = abs(leftheight - rightheight)
        
        if diff <= 1:
            if self.isbalanced(node.left):
                if self.isbalanced(node.right):
                    return True
        return False

    def getheight(self, node):
        if node is None:
            return 0
        
        l = self.getheight(node.left)
        r = self.getheight(node.right)
        return max(l, r) + 1

    def leveltasks(self, node, k):
        if node is None:
            return
            
        queue = [node]
        res = []
        
        while len(queue) > 0:
            current = queue.pop(0)
            res.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            
        print(f"Full Level Order Traversal: {res}")
        print(f"(i) Beginning (First Node): {res[0]}")
        
        lastindex = len(res) - 1
        print(f"(ii) End (Last Node): {res[lastindex]}")
        
        if k > 0:
            if k <= len(res):
                 print(f"(iii) Element at position {k}: {res[k-1]}")
            else:
                 print(f"(iii) Position {k} is out of range.")
        else:
             print(f"(iii) Position {k} is out of range.")

# Driver Code
tree = BinaryTree()
items = [50, 30, 20, 40, 70, 60, 80]

for i in items:
    tree.insert(i)

print("Inorder Traversal:")
tree.inorder(tree.root)

print("\n\nIs Tree Balanced?", tree.isbalanced(tree.root))

print("\n\nLevel Order Tasks:")
tree.leveltasks(tree.root, k=3)