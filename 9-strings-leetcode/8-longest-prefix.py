
"""
Longest prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1: Input: ["flower","flow","flight"] Output: "fl"
Example 2: Input: ["dog","racecar","car"] Output: ""
Explanation: There is no common prefix among the input strings.

"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        slength=len(strs)
        result=''
        if slength<1:
            return result
        if slength==1:
            return strs[0]
        
        for i in range(0, len(strs[0])):
            ch=strs[0][i]
            for j in range(1,slength):
                if ch != strs[j][i]:
                    return result
            result=result+ch
        return result
        
if __name__ == "__main__":