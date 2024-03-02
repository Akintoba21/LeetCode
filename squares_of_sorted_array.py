class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for x in range(len(nums)):
            nums[x] = nums[x] * nums[x]
        nums.sort()
        return nums