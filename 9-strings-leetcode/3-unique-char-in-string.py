
"""
First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
Examples: s = "leetcode" return 0.
s = "loveleetcode", return 2.
Source: 
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/881/

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