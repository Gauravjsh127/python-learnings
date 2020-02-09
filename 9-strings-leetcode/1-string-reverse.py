
"""
Reverse string
Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Source: 

https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
"""

class Solution(object):

    def __init__(self,s):
        """
        initialize your data structure here.
        """
        self.s = s

    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s.reverse()
        
    def reverse(self): 
        st = "" 
        for i in self.s:
            st = i + st
        return st


if __name__ == "__main__":