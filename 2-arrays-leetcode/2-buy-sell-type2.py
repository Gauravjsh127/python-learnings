"""
Buy one and sell one share of the stock multiple times

Source: 

https://www.programcreek.com/2014/02/leetcode-best-time-to-buy-and-sell-stock-ii-java/
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        size = len(prices)
        if size == 0 or size == 1:
            return res

        for i in range(1, size):
            profit = prices[i] - prices[i - 1]
            if profit > 0:
                res = res + profit
        return res

if __name__ == "__main__":