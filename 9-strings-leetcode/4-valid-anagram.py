
"""
Valid anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1: Input: s = "anagram", t = "nagaram" Output: true 
Example 2: Input: s = "rat", t = "car" Output: false

Source: 
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/882/

"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        smap={}
        tmap={}
        for ch in s:
            if ch in smap:
                smap[ch]=smap[ch]+1
            else:
                smap[ch]=1
            
        for ch in t:
            if ch in tmap:
                tmap[ch]=tmap[ch]+1
            else:
                tmap[ch]=1

        if tmap==smap:
            return True
        else:
            return False


if __name__ == "__main__":