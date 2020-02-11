"""
Single link list operations
Source:  https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
"""

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class SLinkList:
    def __init__(self):
        self.head = None

    def display_list(self):
        print('display_list : ')
        node = self.head
        while node != None:
            print(node.data)
            node = node.next

    def add_at_begining(self, newdata):
        newNode = Node(newdata)
        newNode.next = self.head
        self.head = newNode

    def add_at_end(self, newdata):
        newNode = Node(newdata)
        node = self.head
        while node.next != None:
            node = node.next
        node.next = newNode

    def del_at_begining(self):
        node = self.head
        self.head = node.next
        del node

    def del_at_end(self):
        node = self.head
        nextnode = node.next
        while nextnode.next != None:
            node = nextnode
            nextnode = nextnode.next
        node.next = None
        del nextnode

    def reverse_link_list(self):
        curr_node = self.head
        next_node = None
        prev_node = None
        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node


newSlist = SLinkList()
newSlist.add_at_begining(5)
newSlist.add_at_begining(10)
newSlist.add_at_begining(2)
newSlist.display_list()
newSlist.add_at_begining(1)
newSlist.display_list()
newSlist.reverse_link_list()
newSlist.display_list()