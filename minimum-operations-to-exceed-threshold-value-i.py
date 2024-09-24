class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        r = 0
        for x in nums:
            if x < k:
                r += 1
        return r