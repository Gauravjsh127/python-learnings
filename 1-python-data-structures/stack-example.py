"""
Python Stack example : Implemented via list

Summary
The functions associated with stack are:

    empty() – Returns whether the stack is empty – Time Complexity : O(1)
    size() – Returns the size of the stack – Time Complexity : O(1)
    top() – Returns a reference to the top most element of the stack – Time Complexity : O(1)
    push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1)
    pop() – Deletes the top most element of the stack – Time Complexity : O(1)


    Source : https://www.geeksforgeeks.org/stack-in-python/

"""

class solution:
    def __init__(self, mystack=[]):
        """
        Initialization
        """
        self.stack = mystack
        self.maxsize = 10

    def display(self):
        """
        Display stack
        """
        print(self.stack)

    def size(self):
        """
        Display stack size
        """
        print(len(self.stack))

    def push(self, elem):
        """
            Adds the element at the top of the stack – Time Complexity : O(1) 
        """
        if(len(self.stack) == self.maxsize):
            print('Underflow')
            return
        self.stack.append(elem)

    def pop(self):
        """
            Deletes the top most element of the stack – Time Complexity : O(1)
        """
        if(len(self.stack) == 0):
            print('Underflow')
            return
        self.stack.pop()

    def top(self):
        """
            Returns a reference to the top most element of the stack – Time Complexity : O(1)
        """
        print(self.stack[len(self.stack) - 1])

if __name__ == "__main__":
    mystack = [1, 2, 3]
    soln = solution(mystack)
    soln.top()
    soln.push(4)
    soln.top()
    soln.pop()
    soln.top()


