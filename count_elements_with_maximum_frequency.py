class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ndict = {x : nums.count(x) for x in nums}
        mv = max(ndict.values())
        r = 0
        for x,y in ndict.items():
            if y == mv:
                r = r + y
        return r