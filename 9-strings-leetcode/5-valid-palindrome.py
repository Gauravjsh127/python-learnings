
"""
Valid palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Example 1: Input: "A man, a plan, a canal: Panama" Output: true
Example 2: Input: "race a car" Output: false

Source: 
https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/

"""

class Solution(object):
    def isPalindromeBasic(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Run loop from 0 to len/2  
        for i in xrange(0, len(s) / 2):
            
            if s[i] != s[len(s) - i - 1]:
                return False
        return True

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=len(s)
        if l<2:
            return True
        start = 0
        end = l - 1
        while start < end:
            while s[start].isalpha() and start < end:
                start = start + 1
            while s[end].isalpha() and start < end:
                end = end - 1
            if s[start].lower() != s[end].lower() and start < end:
                return False
            else:
                start = start + 1
                end = end - 1
        return True

if __name__ == "__main__":