
"""
First-occurance of substring in string : KMP algorithm

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Example 1: Input: haystack = "hello", needle = "ll" Output: 2
Example 2: Input: haystack = "aaaaa", needle = "bba" Output: -1

Source:

"""

class Solution(object):

    def computePrefix(self, s):
        # time O(n)  space O(n)
        slength=len(s)
        prefix=[0]*slength   
        prefix_index = 0
        suffix_index = 1
        while suffix_index < slength:
            if s[suffix_index] == s[suffix_index]: 
                prefix[suffix_index] = prefix_index + 1
                prefix_index=prefix_index+1
                suffix_index=suffix_index+1
            else:
                if prefix_index:
                    prefix_index = prefix[prefix_index - 1]
                else:
                    suffix_index=suffix_index+1
        return prefix

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # time O(m + n)     // space O(n)
        if len(haystack) ==0:
            return 0;
        if len(needle) ==0:
            return -1;

        prefix=self.computePrefix(haystack)
        i = 0
        j = 0
        m = len(haystack)
        n = len(needle)
        while (i < m):
            if (haystack[i] == needle[j]):
                i=i+1
                j=j+1
            else:
                if j:
                    j = prefix[j - 1]
                else:
                    i=i+1
            if j == n:
                return i - j
        return -1
        
if __name__ == "__main__":