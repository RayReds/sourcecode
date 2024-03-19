inputs = [5, 2, 10, 1, 9, 12]

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class Tree:
    def __init__(self, head):
        self.head = head
    def insert(self, value, parent):
        if self.head == None:
            self.head = Node(value)
        elif parent == None:
            self.insert(self, value, self.head)
        else:
            if value <= parent.value:
                if parent.left is None:
                    parent.left = Node(value)
                else:
                    self.insert(self, value, parent.left)
            else:
                if parent.right is None:
                    parent.right = Node(value)
                else:
                    self.insert(self, value, parent.right)
    def printValues(self):
        pass
BST = Tree()
for i in inputs:
    BST.insert(i, None)
    