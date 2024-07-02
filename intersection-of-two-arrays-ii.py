class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = len(nums1)
        l2 = len(nums2)
        r = []
        if l1 < l2:
            for x in range(l1):
                if nums1[x] in nums2:
                    r.append(nums1[x])
                    nums2.remove(nums1[x])
        else:
            for x in range(l2):
                if nums2[x] in nums1:
                    r.append(nums2[x])
                    nums1.remove(nums2[x])
        return r