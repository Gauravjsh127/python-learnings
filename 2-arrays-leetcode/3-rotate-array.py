
"""
Rotate Array

Source: 

https://www.programcreek.com/2015/03/rotate-array-in-java/
"""

class Solution(object):
    def step_by_step_rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if size == 0 or size == 1 or k == 0:
            return
        for x in range(0, k):
            last = nums[size - 1]
            for j in range(size - 1, 0, -1):
                nums[j] = nums[j - 1]
            nums[0] = last




if __name__ == "__main__":