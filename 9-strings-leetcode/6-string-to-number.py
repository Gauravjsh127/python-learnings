
"""
String to Integer (atoi)

Example 1: Input: "42" Output: 42

Source:
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/884/

"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign = 1
        base = 0
        i = 0;
        while str[i] == ' ':
            i=i+1 
        if str[i] == '-':
            sign = -1
            i=i+1 
        if str[i] == '+' and sign!=-1: 
            sign = 1;
            i=i+1 
        while int(str[i]) >= '0' and int(str[i]) <= '9':
            if (base >  sys.maxint / 10 or (base == sys.maxint / 10 and int(str[i]) > 7)):
                if sign == 1: 
                    return sys.maxint
                else: 
                    return sys.minint            
            base  = 10 * base + int(str[i])
            i=i+1
        return base * sign

if __name__ == "__main__":