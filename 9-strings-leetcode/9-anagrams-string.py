"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Example 1: Input:
s: "cbaebabacd" p: "abc" Output: [0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2: Input: s: "abab" p: "ab"
Output: [0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

https://leetcode.com/problems/find-all-anagrams-in-a-string/

"""

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        smap = {}
        pmap = {}
        res = []
        if (len(s)< len(p)):
            return res
            
        for i in range(0, len(p)):
            in s[i] in smap:
                smap[s[i]] = smap[s[i]] + 1
            else:
                smap[s[i]] = 1
            in p[i] in pmap:
                pmap[p[i]] = pmap[p[i]] + 1
            else:
                pmap[p[i]] = 1


        start = 0
        if smap==pmap:
            res.append(start)
        
        for i in range(len(p), len(s)):
            smap[s[start]] =  smap[s[start]] - 1

            if(smap[s[start]] == 0):
                del smap[s[start]]
            
            start = start + 1 

            in s[i] in smap:
                smap[s[i]] = smap[s[i]] + 1
            else:
                smap[s[i]] = 1

            if smap==pmap:
                res.append(i-len(p)+1)

        return res