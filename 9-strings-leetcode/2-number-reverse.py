
"""
Reverse number

Example 1: Input: 123 Output: 321
Example 2: Input: -123 Output: -321
Example 3: Input: 120 Output: 21

Source: 

https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        while x != 0:
            pop = x % 10
            x /= 10
            if rev > sys.maxint/10 or (rev == sys.maxint / 10 && pop > 7):
                return 0
            if rev < sys.minint/10 or (rev == sys.minint / 10 && pop < -8): 
               return 0
            rev = rev * 10 + pop
        return rev


if __name__ == "__main__":