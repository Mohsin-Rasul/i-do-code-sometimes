
class Node:
    def __init__(self, name, bonus):
        self.name = name
        self.bonus = bonus
        self.left = None
        self.right = None


def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print("Employee:", root.name, "| Bonus:", root.bonus)


ceo = Node("CEO", 10000)
manager1 = Node("Manager A", 7000)
manager2 = Node("Manager B", 7000)
sub1 = Node("Subordinate A", 3000)
sub2 = Node("Subordinate B", 3000)

ceo.left = manager1
ceo.right = manager2
manager1.left = sub1
manager1.right = sub2

post_order(ceo)
