
"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

Source: 

https://leetcode.com/problems/merge-intervals/
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        size = len(intervals)
        if size<2:
            return intervals
        
        intervals_sorted_start_time= sorted(intervals, key = lambda x:x[0])
        
        result = []
        result.append(intervals_sorted_start_time[0])
        
        for i in range(1,size):
            if result[len(result) - 1][1] < intervals_sorted_start_time[i][0]:
                 result.append(intervals_sorted_start_time[i])
            else:
                result[len(result)- 1][1] = max (result[len(result) - 1 ][1],intervals_sorted_start_time[i][1])
        return result
    