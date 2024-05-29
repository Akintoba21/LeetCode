class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for x in range(len(nums)+1):
            count = 0
            for y in nums:
                if (y >= x):
                    count += 1
                    if (count > x): break
            if (count == x):
                return count
        return -1