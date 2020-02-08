
"""
Min stack
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Source: 

https://leetcode.com/problems/min-stack/discuss/500644/Two-Stack-C%2B%2B-solution
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.mins.append(x)
            self.stack.append(x)
            return

        val = self.mins[len(self.mins) - 1]
        if val >= x:
            self.mins.append(x)
        self.stack.append(x)
        return

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack[len(self.stack) - 1]
        if val == self.mins[len(self.mins) - 1]:
            self.mins.pop()
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack) - 1]     

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[len(self.mins) - 1]





if __name__ == "__main__":