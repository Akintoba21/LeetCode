class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        l, r = 0, 0
        m = 0
        while r < len(nums2) and l < len(nums1):
            if nums1[l] <= nums2[r]:
               m = max(m,r-l)
               r += 1
            else:
                l += 1
                r += 1
        return m 