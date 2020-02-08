"""
Remove Duplicates from Sorted Array

Source: 

https://www.geeksforgeeks.org/remove-duplicates-sorted-array/
"""


class Solution(object):
    # Not Using extra space
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0 or size == 1:
            return size

        # To store index of next
        # unique element
        j = 0

        # Doing same as done
        # in Method 1 Just
        # maintaining another
        # updated index i.e. j
        for i in range(0, (size - 1)):
            if nums[i] != nums[i + 1]:
                nums[j] = nums[i]
                j += 1

        nums[j] = nums[size - 1]
        j += 1
        return j


if __name__ == "__main__":

