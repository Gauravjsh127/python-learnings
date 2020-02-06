"""
Python List examples

Summary

Add    
   - append(val) : to end of list
   - insert(pos, val)

Delete
   - remove(val) : delete by value
   - pop(pos optional): delete by position
   - clear()  : delete complete list

size 
   - len(list)

occurance
   - count(val)

sort/reverse
    - sort
    - reverse

"""

class solution:
    def __init__(self, mylist):
        """
        Initialization
        """
        self.list = mylist

    def display(self):
        """
        Display list
        """
        print(self.list)

    def append(self, elem):
        """
        Add an item to the end of the list
        """
        self.list.append(elem)

    def insert(self, pos, elem):
        """
        Insert an item at a given position
        """
        self.list.insert(pos, elem)

    def remove(self, val):
        """
        Remove the first item from the list whose value is equal to val.
        """
        self.list.remove(val)

    def pop(self, pos):
        """
        Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list
        """
        self.list.pop(pos)

    def clear(self):
        """
        Remove all items from the list. Equivalent to del a[:].
        """
        self.list.clear()

    def count(self, val):
        """
        Return the number of times x appears in the list.
        """
        return self.list.count(val)

    def length(self):
        """
        Return the size of the list
        """
        return len(self.list)

    def sort(self):
        """
        Sort the given list
        """
        self.list.sort()

    def reverse(self):
        """
        Reverse the given list
        """
        self.list.reverse()


if __name__ == "__main__":
    mylist = [1, 2, 3]
    soln = solution(mylist)
    soln.display()
    soln.append(4)
    soln.display()
    soln.insert(0, 5)
    soln.display()
    soln.remove(3)
    soln.display()
    soln.pop(2)
    soln.display()
    soln.clear()
    soln.display()
    soln.append(4)
    soln.append(4)
    soln.append(2)
    soln.append(9)
    print(soln.count(4))
    print(soln.length())
    soln.sort()
    soln.display()
    soln.reverse()
    soln.display()
