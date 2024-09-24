class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = map(str,arr1)
        arr2 = map(str,arr2)
        hs = set()
        for x in arr1:
            for y in range(1,len(x)+1):
                hs.add(x[:y])
        r = 1
        for x in arr2:
            while r <= len(x) and x[:r] in hs:
                r += 1
        return r-1