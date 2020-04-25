"""
Top K Frequent WordsYour answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1: Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2 Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words. Note that "i" comes before "love" due to a lower alphabetical order.
Example 2: Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"] Explanation: "the", "is", "sunny" and "day" are the four most frequent words,with the number of occurrence being 4, 3, 2 and 1 respectively.
"""

import random
import collections
from collections import OrderedDict

class Solution(object):
    def __init__(self, k):
        self.k = k
        self.wordDict = {}

    def topKFrequent(self, words):
        for word in words:
            if word in self.wordDict:
                self.wordDict[word] += 1
            else:
                self.wordDict[word] = 1
        # Sort Dict by keys
        OrderedDict(sorted(self.wordDict.items(), key=lambda t: t[1]))
        res = []
        j = 0
        for key in self.wordDict:
            res.append(key)
            if len(res) == self.k:
                return res
        return res


if __name__ == "__main__":
    s = Solution(1)
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    print(s.topKFrequent(words))
