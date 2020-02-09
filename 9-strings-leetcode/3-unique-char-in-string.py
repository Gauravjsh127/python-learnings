
"""
Reverse number

Example 1: Input: 123 Output: 321
Example 2: Input: -123 Output: -321
Example 3: Input: 120 Output: 21

Source: 

https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ll = len(s)
        mmap = {}
        print(mmap)
        for index in range(0, ll):
            if s[index] in mmap:
                mmap[s[index]] = mmap[s[index]] + 1
            else:
                mmap[s[index]] = 1
        print(mmap)
        for index in range(0, ll):
            if mmap[s[index]] == 1:
                return index
        return -1


if __name__ == "__main__":