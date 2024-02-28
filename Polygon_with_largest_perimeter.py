class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lside = max(nums)
        sides = sum(nums) - lside
        while (lside >= sides and len(nums) >= 3):
            nums.remove(lside)
            lside = max(nums)
            sides = sum(nums) - lside
        if len(nums) >= 3: return sum(nums)
        return -1