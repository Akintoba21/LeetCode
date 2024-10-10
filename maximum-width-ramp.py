class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ms = []
        ms.append(0)
        for x in range(1,len(nums)):
            if nums[x] < nums[ms[-1]]: ms.append(x)
        r = 0
        for x in range(len(nums)-1,-1,-1):
            while ms and nums[x] >= nums[ms[-1]]:
                r = max(r,x - ms.pop(-1))
        return r