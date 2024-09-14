class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = max(nums)
        l = 0
        le = len(nums)
        a = 0
        while l < le:
            if nums[l] == n:
                r = l + 1
                while r < le and nums[r] == n:
                    r += 1
                a = max(a,r-l)
                l = r
            else:
                l += 1
        return a