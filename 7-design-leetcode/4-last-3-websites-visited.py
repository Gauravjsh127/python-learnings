"""
Last 3 websites visited

Example 1:  AABBBCCCCDDDDDDABBBBB 
output : BAD
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LastKWebsiteVisited():
    def __init__(self, size):
        self.size = size
        self.head = None    # New entry always added from begining / deletion can be from anywhere
        self.wmap = {}      # key is the website name and value is the list index that stores that website

    def add_at_begining(self, newdata):
        newNode = Node(newdata)
        newNode.next = self.head
        self.head = newNode
        return newNode

    def del_at_end(self):
        node = self.head
        nextnode = node.next
        while nextnode.next != None:
            node = nextnode
            nextnode = nextnode.next
        node.next = None
        val = nextnode.data
        del nextnode
        return val

    def del_based_on_node(self, data):
        #print('data :' + data)
        node = self.head
        if node == None:
            return
        ## Data matches with the very first node
        if (node.data == data):
            self.head = node.next
            del node
            return
        prevnode = None
        while node.data != data:
            prevnode = node
            node = node.next
        prevnode.next = node.next
        del node

    def website_visited(self, website_visited_list):
        for web in website_visited_list:
            #print("New Web URL :" + web)
            if web in self.wmap:
                #print('Already in wmap')
                node = self.wmap[web]
                self.del_based_on_node(node.data)
                self.wmap[web] = self.add_at_begining(web)
            else:
                #print('Not in wmap')
                if len(self.wmap) == self.size:
                    web_least_visited = self.del_at_end()
                    del self.wmap[web_least_visited]
                self.wmap[web] = self.add_at_begining(web)
            #self.print_lask_k_list()

    def print_lask_k_list(self):
        print('Last K web URLS : ')
        node = self.head
        while node != None:
            print(node.data)
            node = node.next


K = 3
obj = LastKWebsiteVisited(K)
WEB_URL_LIST = 'AABBBCCCCDDDDDDABBBBB'
print(WEB_URL_LIST)
obj.website_visited(WEB_URL_LIST)
obj.print_lask_k_list()
