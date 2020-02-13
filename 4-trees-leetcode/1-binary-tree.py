"""
Binary Tree : Add delete  traverse

https://medium.com/@stephenagrice/how-to-implement-a-binary-search-tree-in-python-e1cdba29c533

"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data == data:
            return False
        elif data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def find(self, data):
        if self.data == data:
            return True
        elif data < self.data and self.left:
            return self.left.find(data)
        elif data > self.data and self.right:
            return self.right.find(data)
        return False

    def preorder(self, l):
        l.append(self.data)
        if self.left:
            self.left.preorder(l)
        if self.right:
            self.right.preorder(l)
        return l

    def postorder(self, l):
        if self.left:
            self.left.postorder(l)
        if self.right:
            self.right.postorder(l)
        l.append(self.data)
        return l

    def inorder(self, l):
        if self.left:
            self.left.inorder(l)
        l.append(self.data)
        if self.right:
            self.right.inorder(l)
        return l


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    # return list of data elements resulting from preorder tree traversal
    def preorder(self):
        if self.root:
            return self.root.preorder([])
        else:
            return []

    # return list of postorder elements
    def postorder(self):
        if self.root:
            return self.root.postorder([])
        else:
            return []

    # return list of inorder elements
    def inorder(self):
        if self.root:
            return self.root.inorder([])
        else:
            return []

    # return True if d is found in tree, false otherwise
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

bst = BST()

bst.insert(2)
bst.insert(1)
bst.insert(3)

l = bst.preorder()
print(' Pre order List ')
print(l)

l = bst.postorder()
print(' Post order List ')
print(l)

l = bst.inorder()
print(' In order List ')
print(l)
