class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        r = 1
        i = 0
        while i+r < len(nums):
            if nums[i+r] - nums[i] <= 2*k: r += 1
            else: i += 1
        return r